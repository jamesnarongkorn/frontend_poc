import re
import openai

from fastapi import HTTPException
from langfuse.decorators import observe

from typing import AsyncGenerator

from app import jai_client, typhoon_gemma_12b_client
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
        response = await typhoon_gemma_12b_client.chat.completions.create(
            model='typhoon-gemma-12b',
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


class ImageReplacer:
    def __init__(self, valid_image_ids, repo_image_url_base="https://raw.githubusercontent.com/jamesnarongkorn/frontend_poc/refs/heads/main/renamed_images/"):
        self.repo_image_url_base = repo_image_url_base
        self.processed_image_ids = set()
        self.valid_image_ids = valid_image_ids

    def replace_image_ids_with_markdown(self, text):
        """
        Replaces image IDs in a text with Markdown image links, keeping only the first occurrence of each image.

        Args:
            text (str): The input text containing image IDs (a chunk of streaming data).

        Returns:
            str: The text with image IDs replaced by Markdown image links, with only the first occurrence of each image.
        """
        image_id_regex = re.compile(r"\[IMG:([A-Za-z0-9_.]+\.png)\]")  # Match [IMG:D02_030.png]

        def replace(match):
            image_id = match.group(1)  # Extract the image ID
            if image_id not in self.processed_image_ids and image_id in self.valid_image_ids:
                image_url = f"{self.repo_image_url_base}{image_id}"  # Construct the full image URL
                self.processed_image_ids.add(image_id)  # Mark as processed
                return f"\n\n![{image_id}]({image_url})\n\n"  # Create the Markdown link
            else:
                return ""  # Replace with an empty string if already processed

        return image_id_regex.sub(replace, text)


@observe()
async def generate_rag_answer(conversation_history: str, context: str, image_replacer: ImageReplacer) -> str:
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
        response = await typhoon_gemma_12b_client.chat.completions.create(
            model='typhoon-gemma-12b',
            messages=[
                {'role': 'system', 'content': RAG_PROMPT.format(context=context)},
                {'role': 'user', 'content': prompt},
            ],
            temperature=0.1,
            seed=42,
            stream=False,
        )

        # Extract response content
        response_content = response.choices[0].message.content.strip().replace("_final_with_captions.md", ".pdf")
        print(f'----------\nLLM response_content:\n{response_content}\n----------\n')
        markdown_output = image_replacer.replace_image_ids_with_markdown(response_content)
        print(f'----------\nmarkdown_output:\n{markdown_output}\n----------\n')
        return markdown_output

    except openai.OpenAIError as e:
        print(f'API error - {e}')
        raise HTTPException(status_code=500, detail='Internal Server Error')

    except Exception as e:
        print(f'Error in RAG answer generation: {e}')
        return 'ไม่สามารถเชื่อมต่อกับระบบได้ในขณะนี้ กรุณาลองใหม่ภายหลัง'

@observe()
async def generate_rag_answer_stream(conversation_history: str, context: str, image_replacer: ImageReplacer) -> AsyncGenerator[str, None]:
    """Generates a RAG answer based on the context and query, streaming the response.

    Args:
        conversation_history: The preceding dialogue.
        context (str): The context for the RAG generation.

    Yields:
        str: Chunks of the generated answer.
    """
    prompt = f"""
**[USER QUERY]**
{conversation_history}

**Answer:**
"""

    try:
        response = await typhoon_gemma_12b_client.chat.completions.create(
            model='typhoon-gemma-12b',
            messages=[
                {'role': 'system', 'content': RAG_PROMPT.format(context=context)},
                {'role': 'user', 'content': prompt},
            ],
            temperature=0.1,
            seed=42,
            stream=True,
        )

        state = "streaming_text"  # Can be 'streaming_text' or 'buffering_tag'
        tag_buffer = ""

        async for chunk in response:
            content = chunk.choices[0].delta.content or ""
            for char in content:
                
                # --- STATE: Streaming normal text ---
                if state == "streaming_text":
                    if char == '[':
                        # Potential start of a tag, switch state and start buffering
                        state = "buffering_tag"
                        tag_buffer += char
                    else:
                        # Not a special character, yield it immediately for a smooth stream
                        yield char

                # --- STATE: Buffering a potential tag ---
                elif state == "buffering_tag":
                    tag_buffer += char
                    if char == ']':
                        # Tag is complete, process the entire buffer
                        processed_tag = image_replacer.replace_image_ids_with_markdown(tag_buffer)
                        yield processed_tag
                        
                        # Reset state and buffer to continue streaming text
                        tag_buffer = ""
                        state = "streaming_text"
                    elif char == '[':
                        # Malformed tag, e.g., "[IMG:[...". The previous tag was incomplete.
                        # Flush the old buffer as plain text (except for the new '[')
                        yield tag_buffer[:-1]
                        # Start a new tag buffer with the new '['
                        tag_buffer = '['

        # After the loop, if the stream ends while we're still buffering a tag,
        # it means the tag was incomplete. Flush the buffer as plain text.
        if tag_buffer:
            yield tag_buffer

    except Exception as e:
        print(f'Error in RAG answer generation: {e}')
        yield 'ไม่สามารถเชื่อมต่อกับระบบได้ในขณะนี้ กรุณาลองใหม่ภายหลัง'


@observe()
async def generate_non_rag_answer(conversation_history: str, user_input: str) -> str:
    """Generates a non-RAG answer to a query.

    Args:
        query (str): The user's input query.
        system_prompt (str): The system promptfor the response.

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


async def generate_non_rag_answer_stream(conversation_history: str, user_input: str) -> AsyncGenerator[str, None]:
    """Generates a non-RAG answer to a query, streaming the response.

    Args:
        conversation_history (str): The previous conversation history.
        user_input (str): The user's input query.

    Yields:
        str: Chunks of the generated answer.
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
            stream=True,
        )

        async for chunk in response:
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                chunk_content = chunk.choices[0].delta.content
                yield chunk_content

    except openai.APIError as e:
        print(f'API error - {e}')
        yield 'Internal Server Error' # Consider a more user-friendly message.
        raise HTTPException(status_code=500, detail='Internal Server Error')

    except Exception as e:
        print(f'Error in non-RAG answer generation: {e}')
        yield 'ไม่สามารถเชื่อมต่อกับระบบได้ในขณะนี้ กรุณาลองใหม่ภายหลัง'


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
        response = await typhoon_gemma_12b_client.chat.completions.create(
            model='typhoon-gemma-12b',
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
