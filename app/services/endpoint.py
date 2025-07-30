# app/api/endpoints.py

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

# Import your business logic function and request/response models
from app.services.chat_poc import get_chat_response

# Create a new router
# This can be included in your main FastAPI app
router = APIRouter()

class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    message: str
    
class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    streaming: bool = Field(
        default=False, 
        description="Flag to determine if the response should be streamed."
    )

class ChatResponse(BaseModel):
    response: str
    sources: List[str]
    intent: Optional[str] = None # Make intent optional as it might not always be returned


@router.post(
    "/chat",
    # We explicitly declare the non-streaming response model for OpenAPI docs.
    # The streaming response is handled separately.
    response_model=ChatResponse, 
    summary="Handle a chat conversation",
    description="""
Processes a list of messages. 
- If `streaming` is `false` (default), it returns a JSON object with the full response.
- If `streaming` is `true`, it returns a Server-Sent Events (SSE) stream.
"""
)
async def handle_chat_request(request: ChatRequest):
    """
    This endpoint serves as the web interface for the chat logic. 
    It receives a request, calls the core `get_chat_response` function,
    and then correctly formats the output as either a standard JSON response
    or a streaming response.
    """
    # The `if/else` block is the key to solving the original problem.
    # We check the `streaming` flag and handle each case differently.

    if request.streaming:
        # --- STREAMING RESPONSE ---
        # The logic function returns an async generator.
        # We must wrap it in a StreamingResponse to send it to the client.
        try:
            # We call your function with streaming=True
            stream_generator = await get_chat_response(
                messages=[msg.model_dump() for msg in request.messages], 
                streaming=True
            )
            # Use "text/event-stream" for Server-Sent Events (SSE), a standard for streaming.
            return StreamingResponse(stream_generator, media_type="text/event-stream")
        except Exception as e:
            # This handles errors that might occur before the stream even starts
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while initiating the stream: {e}"
            )

    else:
        # --- NON-STREAMING (JSON) RESPONSE ---
        # The logic function returns a dictionary.
        # FastAPI can automatically convert this to a JSON response.
        try:
            # We call your function with streaming=False
            response_dict = await get_chat_response(
                messages=[msg.model_dump() for msg in request.messages], 
                streaming=False
            )
            # The 'response_model=ChatResponse' in the decorator will validate this dictionary.
            return response_dict
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while processing the request: {e}"
            )