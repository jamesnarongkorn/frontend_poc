import re
from typing import Union, List, Dict, Any, Literal

from fastapi import APIRouter, HTTPException
from langfuse.decorators import langfuse_context, observe

from app.utils.models import ChatRequest, ChatResponse
from .llm_calls import classify_intent, generate_rag_answer, generate_non_rag_answer, rewrite_query
from .rag_service import perform_hybrid_search


router = APIRouter()


# langfuse_context.configure(environment='poc')

def format_docs_for_rag(docs: list) -> str:
    """
    Formats a list of document chunks into a single string for RAG context.
    
    Args:
        docs (list): A list of dictionaries, where each dict is a search result.
        
    Returns:
        str: A single string containing all formatted document content.
    """    
    formatted_context = []
    for i, doc in enumerate(docs):
        # Create a structured block for each document
        context_block = f"""---
Context Document {i+1}:
Content: {doc.get('chunk_content', '').strip()}
Source: {doc.get('source_document', 'N/A')}
---"""
        formatted_context.append(context_block)
        
    # Join all blocks into a single string, separated by newlines
    return "\n\n".join(formatted_context)


@router.post('/chat', response_model=ChatResponse)
@observe()
async def chat_endpoint(
    request: ChatRequest,
):
    """
    ## Chat Endpoint for Handling User Queries

    **Purpose**
    This endpoint processes user chat requests, determines whether retrieval-augmented generation (RAG) is needed, and generates responses accordingly.

    **Request Body (JSON)**
    Expects a JSON object that FastAPI parses into a Pydantic model (`ChatRequest`):
    - **request** (List[MessageItem]): A list of messages representing the conversation history. Each entry contains:
        - `role` (str): The role of the sender (`user` or `assistant`).
        - `message` (str): The message content.

    **Response (JSON)**
    Returns a JSON object that FastAPI serializes from a Pydantic model (`ChatResponse` or `ChatEvalResponse`):
    - `response` (str): The generated response message.
    - `source_documents` (Optional[List[str]]: An optional field for additional context.

    **Example**
    - **User Query and Response**:

      **Request:**
      ```json
      {
          "request": [
              {
                  "message": "ถ้าเสียบเครื่องรูดบัตรแล้วยังใช้ไม่ได้ ต้องทำยังไงต่อ",
                  "role": "user"
              }
          ]
      }
      ```

      **Response:**
      ```json
      {
          "response": "reponse",
          "source_documents": [
          ],
      }
      ```
    """

    try:
        print('\n=== New Request ===')

        # Validate request body
        if not request.request:
             raise HTTPException(status_code=400, detail="Request list cannot be empty.")

        # Get conversation history as a single string
        conversation_history = '\n'.join(f'{item.role}: {item.message}' for item in request.request)
        user_messages = [item.message for item in request.request if item.role == 'user']
        user_input = user_messages[-1].strip() if user_messages else 'สวัสดี'

        # langfuse_context.update_current_trace(user_id=request.user_id, session_id=f"{user_input}")

        # 1. Classify Intent
        print(f"\n--- Classifying Intent for: '{user_input}' ---")
        intent = await classify_intent(conversation_history, user_input)
        print(f'Classified Intent: {intent}')

        if intent == "other":
            response = await generate_non_rag_answer(conversation_history, user_input)

            print(f'Generated Non-RAG response: {response}')
            return ChatResponse(response=response, source_documents=None, intent=intent)

        # 2. Rewrite query
        rewritten_query = await rewrite_query(conversation_history)

        if not rewritten_query:
            rewritten_query = user_input

        print(f'Rewritten Query: {rewritten_query}')
        print('\n')

        if intent == "RAG":
            docs = await perform_hybrid_search(rewritten_query)
            formatted_context = format_docs_for_rag(docs)
            response = await generate_rag_answer(formatted_context, user_input)

        response_data = {
            "response": response,
            "source_documents": [doc.get('chunk_content', '') for doc in docs] if docs else None,
            "intent": intent,
        }

        print(f'\n=== Request End ===')

        return ChatResponse(**response_data)

    except HTTPException as http_e:
        # Re-raise HTTP exceptions from FastAPI/manual checks
        raise http_e
    except Exception as e:
        # Catch-all for unexpected errors during orchestration
        print(f'!!! Critical Error in chat_endpoint orchestrator: {e}')
        import traceback
        traceback.print_exc() # Print stack trace for debugging

        # Return a generic error response
        # Ensure token counts are returned even in case of error
        return ChatResponse(
            response="ขออภัยค่ะ เกิดข้อผิดพลาดบางอย่าง โปรดลองใหม่อีกครั้งในภายหลัง",
        )