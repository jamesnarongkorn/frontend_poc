import json, re
import traceback
from typing import AsyncGenerator, List, Dict
from FlagEmbedding import FlagReranker

from langfuse.decorators import langfuse_context, observe

from app.utils.models import ChatRequest, ChatResponse
from .llm_calls import (
    classify_intent, 
    generate_rag_answer, 
    generate_rag_answer_stream, 
    generate_non_rag_answer, 
    generate_non_rag_answer_stream, 
    rewrite_query, 
    ImageReplacer,
)
from .rag_service import perform_hybrid_search
from app import image_collection

# This separator constant is now used by both chat_logic.py and streamlit.py
SOURCES_SEPARATOR = "---_SOURCES_SEPARATOR_---"

# Configure langfuse once
langfuse_context.configure(environment='poc')

def format_docs_for_rag(docs: list) -> str:
    """
    Formats a list of document chunks into a single string for RAG context.
    """    
    formatted_context = []
    for i, doc in enumerate(docs):
        context_block = f"""---
Context Document {i+1}:
Context: {doc.get('contextual_summary', '').strip()}
Content: {doc.get('chunk_content', '').strip()}
Source: {doc.get('source_document', 'N/A')}
---"""
        formatted_context.append(context_block)
    final_context = "\n\n".join(formatted_context)
    # cleaned_text = re.sub(r"<!--.*?-->", "", final_context)
    return final_context

def format_docs_for_rag(docs: list) -> str:
    """
    Formats a list of document chunks into a single string for RAG context.
    """    
    formatted_context = []
    for i, doc in enumerate(docs):
        context_block = f"""---
Context Document {i+1}:
Context: {doc.get('contextual_summary', '').strip()}
Content: {doc.get('chunk_content', '').strip()}
Source: {doc.get('source_document', 'N/A')}
---"""
        formatted_context.append(context_block)
    final_context = "\n\n".join(formatted_context)
    # cleaned_text = re.sub(r"<!--.*?-->", "", final_context)
    return final_context

def format_docs_for_reranker(docs: list) -> list:
    """
    Formats a list of document chunks into a list of strings,
    where each string represents a single document chunk formatted for reranking.
    """
    formatted_documents = []
    for i, doc in enumerate(docs):
        context_block = f"""Context: {doc.get('contextual_summary', '').strip()}\n
Content: {doc.get('chunk_content', '').strip()}\n
Source: {doc.get('source_document', 'N/A')}
"""
        formatted_documents.append(context_block)  # Append each document as a string

    return formatted_documents  # Return a list of strings

reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)

@observe()
async def get_chat_response(
    messages: List[Dict],
    streaming: bool = False
) -> AsyncGenerator[str, None] | Dict:
    """
    This function replaces the FastAPI endpoint logic. It can return either:
    1. A dictionary (for non-streaming).
    2. An async generator (for streaming).
    """
    try:
        print('\n=== New Request ===')
        
        if not messages:
            raise ValueError("Messages list cannot be empty.")

        conversation_history = '\n'.join(f'{item["role"]}: {item["message"]}' for item in messages)
        user_messages = [item["message"] for item in messages if item["role"] == 'user']
        user_input = user_messages[-1].strip() if user_messages else 'สวัสดี'

        print(f"\n--- Classifying Intent for: '{user_input}' ---")
        intent = await classify_intent(conversation_history, user_input)
        print(f'Classified Intent: {intent}')

    except Exception as e:
        print(f'!!! Critical Error during initial setup: {e}')
        if streaming:
            async def error_stream():
                yield "An error occurred while processing your request."
            return error_stream()
        else:
            return {"response": "An error occurred while processing your request.", "sources": []}

    image_ids = image_collection.find({}, {"image_id": 1, "_id": 0})
    valid_image_ids = [f'{doc["image_id"]}.png' for doc in image_ids]

    # --- STREAMING LOGIC ---
    if streaming:
        async def stream_generator() -> AsyncGenerator[str, None]:
            source_docs_content = []
            try:
                if intent == "RAG":
                    rewritten_query = await rewrite_query(conversation_history) or user_input
                    print(f'Rewritten Query: {rewritten_query}')
                    docs = await perform_hybrid_search(rewritten_query)
                    formatted_context = format_docs_for_reranker(docs)

                    input_pairs = [(rewritten_query, doc) for doc in formatted_context]
                    scores = reranker.compute_score(input_pairs)
                    document_scores = list(zip(formatted_context, scores))
                    ranked_documents = sorted(document_scores, key=lambda x: x[1], reverse=True)
                    ranked_documents = [doc[0] for doc in ranked_documents[:5]]
                    print(f"Ranked Documents: {ranked_documents}")
                    # source_docs_content = [doc.get('chunk_content', '') for doc in docs]
                    
                    yield json.dumps(ranked_documents) + '\n'
                    yield SOURCES_SEPARATOR + '\n'

                    local_image_replacer = ImageReplacer(valid_image_ids=valid_image_ids)
                    async for chunk in generate_rag_answer_stream(ranked_documents, user_input, local_image_replacer):
                        yield chunk
                
                else: # "other" or any other intent
                    yield json.dumps([]) + '\n'
                    yield SOURCES_SEPARATOR + '\n'
                    async for chunk in generate_non_rag_answer_stream(conversation_history, user_input):
                        yield chunk

            except Exception as e:
                print(f'!!! Critical Error during stream generation: {e}')
                traceback.print_exc()
                yield "\n\nขออภัยค่ะ เกิดข้อผิดพลาดบางอย่าง โปรดลองใหม่อีกครั้งในภายหลัง"
        
        # Return the async generator itself
        return stream_generator()

    # --- NON-STREAMING LOGIC ---
    else:
        try:
            response_content = ""
            source_docs = []

            if intent == "RAG":
                local_image_replacer = ImageReplacer(valid_image_ids=valid_image_ids)
                rewritten_query = await rewrite_query(conversation_history) or user_input
                print(f'Rewritten Query: {rewritten_query}')

                docs = await perform_hybrid_search(rewritten_query)
                formatted_context = format_docs_for_rag(docs)
                response_content = await generate_rag_answer(formatted_context, user_input, local_image_replacer)
                source_docs = [doc.get('chunk_content', '') for doc in docs]
            
            else: # "other" or any other intent
                response_content = await generate_non_rag_answer(conversation_history, user_input)

            print(f'\n=== Request End ===')
            return {
                "response": response_content,
                "sources": source_docs,
                "intent": intent
            }

        except Exception as e:
            print(f'!!! Critical Error in non-streaming orchestration: {e}')
            traceback.print_exc()
            return {"response": "ขออภัยค่ะ เกิดข้อผิดพลาดบางอย่าง โปรดลองใหม่อีกครั้งในภายหลัง", "sources": []}