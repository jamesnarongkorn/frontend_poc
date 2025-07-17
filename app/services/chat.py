import json
from typing import AsyncGenerator

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from langfuse.decorators import langfuse_context, observe

from app.utils.models import ChatRequest, ChatResponse, StreamEvent
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

router = APIRouter()

langfuse_context.configure(environment='poc')

SOURCES_SEPARATOR = "---_SOURCES_SEPARATOR_---"

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

@router.post('/chat')
@observe()
async def chat_endpoint(
    request: ChatRequest,
    streaming: bool = False,
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

    except Exception as e:
        print(f'!!! Critical Error during initial setup: {e}')
        # Handle early errors before we decide on streaming vs. not
        if streaming:
            async def error_stream():
                yield "An error occurred while processing your request."
            return StreamingResponse(error_stream(), media_type="text/plain")
        else:
            raise HTTPException(status_code=500, detail="An error occurred while processing your request.")

    image_ids = image_collection.find({}, {"image_id": 1, "_id": 0})
    valid_image_ids = [f'{doc["image_id"]}.png' for doc in image_ids]

    if streaming:        
        async def stream_generator() -> AsyncGenerator[str, None]:            
            """
            Generator that yields sources as a JSON line, a separator, 
            and then the streamed text response.
            """
            source_docs = []
            try:
                if intent == "RAG":
                    rewritten_query = await rewrite_query(conversation_history) or user_input
                    print(f'Rewritten Query: {rewritten_query}')
                    docs = await perform_hybrid_search(rewritten_query)
                    formatted_context = format_docs_for_rag(docs)
                    
                    # Prepare sources to be sent first
                    source_docs = [doc.get('chunk_content', '') for doc in docs]
                    
                    # 1. Yield sources as a single JSON string line
                    yield json.dumps(source_docs) + '\n'
                    # 2. Yield the separator
                    yield SOURCES_SEPARATOR + '\n'

                    # 3. Stream the text chunks from the LLM
                    local_image_replacer = ImageReplacer(valid_image_ids=valid_image_ids)
                    async for chunk in generate_rag_answer_stream(formatted_context, user_input, local_image_replacer):
                        print(chunk)
                        yield chunk
                
                else:
                    # 1. Yield an empty list for sources
                    yield json.dumps([]) + '\n'
                    # 2. Yield the separator
                    yield SOURCES_SEPARATOR + '\n'
                    
                    # 3. Stream the non-RAG answer
                    async for chunk in generate_non_rag_answer_stream(conversation_history, user_input):
                        print(chunk)
                        yield chunk

            except Exception as e:
                print(f'!!! Critical Error during stream generation: {e}')
                import traceback
                traceback.print_exc()
                # If an error happens mid-stream, we can't send sources anymore.
                # Just yield the error message. The client will handle it.
                yield "\n\nขออภัยค่ะ เกิดข้อผิดพลาดบางอย่าง โปรดลองใหม่อีกครั้งในภายหลัง"

        # Return the generator. Note the media_type is now text/plain.
        return StreamingResponse(stream_generator(), media_type="text/plain")

    # --- PATH B: NON-STREAMING (JSON) RESPONSE ---
    else:
        try:
            response_content = ""
            source_docs = None

            if intent == "other":
                response_content = await generate_non_rag_answer(conversation_history, user_input)
                print(f'Generated Non-RAG response: {response_content}')

            elif intent == "RAG":
                local_image_replacer = ImageReplacer(valid_image_ids=valid_image_ids)
                rewritten_query = await rewrite_query(conversation_history) or user_input
                print(f'Rewritten Query: {rewritten_query}')

                docs = await perform_hybrid_search(rewritten_query)
                formatted_context = format_docs_for_rag(docs)
                response_content = await generate_rag_answer(formatted_context, user_input, local_image_replacer)
                source_docs = [doc.get('chunk_content', '') for doc in docs]

            else:
                # Default behavior for any other intents
                response_content = await generate_non_rag_answer(conversation_history, user_input)

            print(f'\n=== Request End ===')
            return ChatResponse(
                response=response_content,
                source_documents=source_docs,
                intent=intent
            )

        except Exception as e:
            print(f'!!! Critical Error in non-streaming orchestration: {e}')
            import traceback
            traceback.print_exc()
            return ChatResponse(response="ขออภัยค่ะ เกิดข้อผิดพลาดบางอย่าง โปรดลองใหม่อีกครั้งในภายหลัง")


# @router.post('/chat', response_model=ChatResponse)
# @observe()
# async def chat_endpoint(
#     request: ChatRequest,
# ):
#     """
#     ## Chat Endpoint for Handling User Queries

#     **Purpose**
#     This endpoint processes user chat requests, determines whether retrieval-augmented generation (RAG) is needed, and generates responses accordingly.

#     **Request Body (JSON)**
#     Expects a JSON object that FastAPI parses into a Pydantic model (`ChatRequest`):
#     - **request** (List[MessageItem]): A list of messages representing the conversation history. Each entry contains:
#         - `role` (str): The role of the sender (`user` or `assistant`).
#         - `message` (str): The message content.

#     **Response (JSON)**
#     Returns a JSON object that FastAPI serializes from a Pydantic model (`ChatResponse` or `ChatEvalResponse`):
#     - `response` (str): The generated response message.
#     - `source_documents` (Optional[List[str]]: An optional field for additional context.

#     **Example**
#     - **User Query and Response**:

#       **Request:**
#       ```json
#       {
#           "request": [
#               {
#                   "message": "ถ้าเสียบเครื่องรูดบัตรแล้วยังใช้ไม่ได้ ต้องทำยังไงต่อ",
#                   "role": "user"
#               }
#           ]
#       }
#       ```

#       **Response:**
#       ```json
#       {
#           "response": "reponse",
#           "source_documents": [
#           ],
#       }
#       ```
#     """

#     try:
#         print('\n=== New Request ===')

#         # Validate request body
#         if not request.request:
#              raise HTTPException(status_code=400, detail="Request list cannot be empty.")

#         # Get conversation history as a single string
#         conversation_history = '\n'.join(f'{item.role}: {item.message}' for item in request.request)
#         user_messages = [item.message for item in request.request if item.role == 'user']
#         user_input = user_messages[-1].strip() if user_messages else 'สวัสดี'

#         langfuse_context.update_current_trace(session_id=f"{user_input}")

#         # 1. Classify Intent
#         print(f"\n--- Classifying Intent for: '{user_input}' ---")
#         intent = await classify_intent(conversation_history, user_input)
#         print(f'Classified Intent: {intent}')

#         if intent == "other":
#             response = await generate_non_rag_answer(conversation_history, user_input)

#             print(f'Generated Non-RAG response: {response}')
#             return ChatResponse(response=response, source_documents=None, intent=intent)

#         # 2. Rewrite query
#         rewritten_query = await rewrite_query(conversation_history)

#         if not rewritten_query:
#             rewritten_query = user_input

#         print(f'Rewritten Query: {rewritten_query}')
#         print('\n')

#         if intent == "RAG":
#             docs = await perform_hybrid_search(rewritten_query)
#             formatted_context = format_docs_for_rag(docs)
#             response = await generate_rag_answer(formatted_context, user_input)

#         response_data = {
#             "response": response,
#             "source_documents": [doc.get('chunk_content', '') for doc in docs] if docs else None,
#             "intent": intent,
#         }

#         print(f'\n=== Request End ===')

#         return ChatResponse(**response_data)

#     except HTTPException as http_e:
#         # Re-raise HTTP exceptions from FastAPI/manual checks
#         raise http_e
#     except Exception as e:
#         # Catch-all for unexpected errors during orchestration
#         print(f'!!! Critical Error in chat_endpoint orchestrator: {e}')
#         import traceback
#         traceback.print_exc() # Print stack trace for debugging

#         # Return a generic error response
#         # Ensure token counts are returned even in case of error
#         return ChatResponse(
#             response="ขออภัยค่ะ เกิดข้อผิดพลาดบางอย่าง โปรดลองใหม่อีกครั้งในภายหลัง",
#         )