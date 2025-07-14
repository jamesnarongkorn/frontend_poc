import json
import re
import ast
import openai

from fastapi import HTTPException
from langfuse.decorators import observe

from typing import Dict, Literal, Optional, Any, List
from pydantic import BaseModel

from app import jai_client
from app.utils.system_prompts import (
    CLASSIFICATION_PROMPT,
    RAG_PROMPT,
    NON_RAG_PROMPT,
    REWRITE_PROMPT,
)

async def generate_query_embedding(text: str) -> list[float]:
    """Generate query embeddings using jai_client asynchronously.

    Args:
        text (str): The input text to generate embeddings for.

    Returns:
        List[float]: The embedding vector.

    """
    try:
        response = await jai_client.embeddings.create(input=text, model='jai-emb-query')
        return response.data[0].embedding

    except Exception as e:
        print(f'Error generating query embedding: {e}')
        return []


@observe()
async def classify_intent(conversation_history: str, user_input: str) -> str:
    """
    Classifies the user's intent based on conversation history and the latest message.

    Args:
        conversation_history: The full conversation history as a string.
        user_input: The latest message from the user.

    Returns:
        A string representing the classified intent: "RAG" or "other".
    """

    prompt = f"""**Context for Analysis:**
Conversation History:
{conversation_history}

User Input: "{user_input}"

**Your Classification:**

Classification (RAG or other):"""

    try:
        response = await jai_client.chat.completions.create(
            model='jai-chat-1-3-2',
            messages=[
                {'role': 'system', 'content': CLASSIFICATION_PROMPT},
                {'role': 'user', 'content': prompt},
            ],
            temperature=0.1,
            seed=42,
        )

        # Clean up the response
        response_text = response.choices[0].message.content.strip().lower()
        if "rag" in response_text.lower():
            classified_intent = "RAG"
        else:
            classified_intent = "other" # Default fallback

        print(f"LLM Classification Raw: '{response_text}', Final Intent: {classified_intent}")
        return classified_intent

    except Exception as e:
        print(f"Error during intent classification: {e}")
        return "product_search"



@observe()
async def generate_rag_answer(conversation_history: str, context: str) -> str:
    """Generates a RAG answer based on the context and query.

    Args:
        conversation_history: The preceding dialogue.
        context (str): The context for the RAG generation.

    Returns:
        str: The generated RAG answer.
    """
    prompt = f"""
**[USER QUERY]**
{conversation_history}

**Answer:**
"""
    
    try:
        response = await jai_client.chat.completions.create(
            model='jai-chat-1-3-2',
            messages=[
                {'role': 'system', 'content': RAG_PROMPT.format(context=context)},
                {'role': 'user', 'content': prompt},
            ],
            temperature=0.1,
            seed=42,
        )

        # Extract response content
        response_content = response.choices[0].message.content.strip().replace("_final_with_captions.md", ".pdf")
        print(f'----------\nLLM response_content:\n{response_content}\n----------\n')
        return response_content

    except openai.OpenAIError as e:
        print(f'API error - {e}')
        raise HTTPException(status_code=500, detail='Internal Server Error')

    except Exception as e:
        print(f'Error in RAG answer generation: {e}')
        return 'ไม่สามารถเชื่อมต่อกับระบบได้ในขณะนี้ กรุณาลองใหม่ภายหลัง'


@observe()
async def generate_non_rag_answer(conversation_history: str, user_input: str) -> str:
    """Generates a non-RAG answer to a query.

    Args:
        query (str): The user's input query.
        system_prompt (str): The system promptfor the response.
        token_tracker (TokenTracker): An instance of TokenTracker to record token usage.

    Returns:
        str: The generated answer.
    """
    prompt = f"""
Previous conversation:
{conversation_history}

The user just said:
{user_input}

Your response:
"""
    try:
        response = await jai_client.chat.completions.create(
            model='jai-chat-1-3-2',
            messages=[
                {'role': 'system', 'content': NON_RAG_PROMPT},
                {'role': 'user', 'content': prompt},
            ],
            temperature=0.5,
            seed=42,
        )

        response_content = response.choices[0].message.content.strip()
        print(f'LLM Non-RAG response_content:\n{response_content}\n')
        return response_content

    except openai.APIError as e:
        print(f'API error - {e}')
        raise HTTPException(status_code=500, detail='Internal Server Error')

    except Exception as e:
        print(f'Error in non-RAG answer generation: {e}')
        return 'ไม่สามารถเชื่อมต่อกับระบบได้ในขณะนี้ กรุณาลองใหม่ภายหลัง'


@observe()
async def rewrite_query(conversation_history: str) -> dict:
    """Rewrites the latest user query into a self-contained search query.

    Args:
        conversation_history (str): The conversation history as a single string.

    Returns:
        dict: A dictionary containing:
            - "rewritten_query": The rewritten, self-contained search query.
    """
    prompt = f"""**Conversation History:**
{conversation_history}

**Rewritten Question:**"""

    try:
        response = await jai_client.chat.completions.create(
            model='jai-chat-1-3-2',
            messages=[
                {'role': 'system', 'content': REWRITE_PROMPT},
                {'role': 'user', 'content': prompt},
            ],
            temperature=0.1,
            seed=42,
        )

        # Extract response
        response_content = response.choices[0].message.content.strip('"').strip()
        return response_content

    except openai.OpenAIError as e:
        print(f'API error - {e}')
        raise HTTPException(status_code=500, detail='Internal Server Error')

    except Exception as e:
        print(f'Error in query rewriting: {e}')
        return {'rewritten_query': ''}
