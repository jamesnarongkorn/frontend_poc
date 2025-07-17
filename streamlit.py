import streamlit as st
import requests
import json

# Page Configuration 
st.set_page_config(
    page_title="BMA Document Chatbot",
    layout="wide"
)
# Inline Title with Logo on the Right 
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <h1 style="margin: 0;">BMA Document Chatbot</h1>
        <img src="https://officialadmin.bangkok.go.th/upload/web_header_logo_CgbiVyAGYL173505.png" width="60" style="margin-right: 15px;">
    </div>
    <p>แชทบอทสำหรับตอบคำถามเกี่ยวกับระบบ MIS ของกรุงเทพมหานคร</p>
    """,
    unsafe_allow_html=True
)

# Configuration
FASTAPI_BASE_URL = "http://127.0.0.1:8000/api/v1/chat"
CHAT_ENDPOINT_NORMAL = f"{FASTAPI_BASE_URL}"
CHAT_ENDPOINT_STREAM = f"{FASTAPI_BASE_URL}?streaming=true"
SOURCES_SEPARATOR = "---_SOURCES_SEPARATOR_---"

use_streaming = st.toggle("Enable Streaming Response", value=True)

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Create a container for the chat history
chat_container = st.container(border=True)

# Display Chat History from session state
with chat_container:
    for message_data in st.session_state.messages:
        # `message_data` is a dict like {"role": "...", "message": "...", "sources": [...]}
        with st.chat_message(message_data["role"]):
            st.markdown(message_data["message"])
            # If the message is from the assistant and has sources, display them
            if "sources" in message_data and message_data["sources"]:
                with st.expander("View Sources"):
                    for i, source in enumerate(message_data["sources"]):
                        # Ensure source is a string before replacing
                        source_text = str(source).replace("#", "")
                        st.info(f"Source {i+1}:\n\n---\n\n{source_text}")

# --- User Input Handling ---
# This block now ONLY handles adding the user's message and triggering a rerun.
if prompt := st.chat_input("พิมพ์คำถามที่ต้องการ..."):
    st.session_state.messages.append({"role": "user", "message": prompt})
    st.rerun()

# --- Generate and Display Assistant Response ---
# This block runs only when the last message is from the user.
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    with chat_container:
        with st.chat_message("assistant"):
            api_request_payload = {"request": st.session_state.messages}

            # --- Streaming Logic ---
            if use_streaming:
                message_placeholder = st.empty()
                full_response = ""
                sources = []
                header_buffer = ""
                header_found = False

                try:
                    with requests.post(CHAT_ENDPOINT_STREAM, json=api_request_payload, stream=True) as response:
                        response.raise_for_status()
                        
                        # Use iter_content to get raw chunks for true streaming effect
                        for chunk in response.iter_content(chunk_size=512, decode_unicode=True):
                            if not chunk:
                                continue

                            # If we haven't found the header yet, add chunk to buffer
                            if not header_found:
                                header_buffer += chunk
                                separator_with_newline = SOURCES_SEPARATOR + '\n'
                                
                                # Check if the separator is now in our buffer
                                if separator_with_newline in header_buffer:
                                    header_found = True
                                    
                                    # Split the buffer to isolate the header and the first part of the text
                                    header_part, initial_text_chunk = header_buffer.split(separator_with_newline, 1)
                                    
                                    try:
                                        sources = json.loads(header_part)
                                    except json.JSONDecodeError:
                                        # This happens if the backend sent an error before the separator.
                                        # Treat the whole buffer as content.
                                        st.warning("Could not parse sources from the stream.")
                                        full_response += header_buffer

                                    else:
                                        # Success, now add the first text chunk to the response
                                        full_response += initial_text_chunk
                                    
                                    message_placeholder.markdown(full_response + "▌")

                            else: # Header was already found, so this is just text
                                full_response += chunk
                                message_placeholder.markdown(full_response + "▌")

                    # If the stream ends before finding the separator, the entire buffer is the response
                    if not header_found:
                        full_response = header_buffer

                    # Final update after the stream is complete
                    message_placeholder.markdown(full_response)

                    # Display sources if they were found
                    if sources:
                        with st.expander("View Sources", expanded=False):
                            for i, source in enumerate(sources):
                                source_text = str(source).replace("#", "")
                                st.info(f"Source {i+1}:\n\n---\n\n{source_text}")
                    
                    # Save the complete response and sources to session state
                    st.session_state.messages.append({
                        "role": "assistant",
                        "message": full_response,
                        "sources": sources 
                    })

                except requests.exceptions.RequestException as e:
                    st.error(f"Could not connect to the backend API. Error: {e}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")

            # --- Non-Streaming Logic ---
            else:
                with st.spinner("Thinking..."):
                    try:
                        response = requests.post(CHAT_ENDPOINT_NORMAL, json=api_request_payload)
                        response.raise_for_status()

                        data = response.json()
                        llm_response = data.get("response", "Sorry, I couldn't get a response.")
                        source_chunks = data.get("source_documents", [])

                        st.markdown(llm_response)

                        if source_chunks:
                            with st.expander("View Sources"):
                                for i, source in enumerate(source_chunks):
                                    source_text = str(source).replace("#", "")
                                    st.info(f"Source {i+1}:\n\n---\n\n{source_text}")

                        st.session_state.messages.append({
                            "role": "assistant",
                            "message": llm_response,
                            "sources": source_chunks
                        })

                    except requests.exceptions.RequestException as e:
                        error_message = f"Could not connect to the backend API. Error: {e}"
                        st.error(error_message)
                    except Exception as e:
                        error_message = f"An unexpected error occurred: {e}"
                        st.error(error_message)


### NON-STREAMING VERSION
# import streamlit as st
# import asyncio

# from app.services.chat import chat_endpoint
# from app.utils.models import ChatRequest

# # Page Configuration
# st.set_page_config(
#     page_title="BMA Document Chatbot",
#     layout="wide"
# )

# # Inline Title with Logo on the Right
# st.markdown(
#     """
#     <div style="display: flex; align-items: center;">
#         <h1 style="margin: 0;">BMA Document Chatbot</h1>
#         <img src="https://officialadmin.bangkok.go.th/upload/web_header_logo_CgbiVyAGYL173505.png" width="60" style="margin-right: 15px;">
#     </div>
#     <p>แชทบอทสำหรับตอบคำถามเกี่ยวกับระบบ MIS ของกรุงเทพมหานคร</p>
#     """,
#     unsafe_allow_html=True
# )

# # Session State Initialization
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Create a container for the chat history
# chat_container = st.container(border=True)

# # Display Chat History
# with chat_container:
#     for message_data in st.session_state.messages:
#         with st.chat_message(message_data["role"]):
#             st.markdown(message_data["message"])
#             if "sources" in message_data and message_data["sources"]:
#                 with st.expander("View Sources"):
#                     for i, source in enumerate(message_data["sources"]):
#                         st.info(f"Source {i+1}:\n\n---\n\n{source}".replace("#", ""))

# # User Input Handling
# if prompt := st.chat_input("พิมพ์คำถามที่ต้องการ..."):
#     st.session_state.messages.append({"role": "user", "message": prompt})
#     st.rerun()


# # Generate and display assistant response
# if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
#     last_user_message = st.session_state.messages[-1]

#     # Display a spinner inside a placeholder in the container
#     with chat_container:
#         with st.chat_message("assistant"):
#             with st.spinner("กำลังประมวลผล..."):
#                 try:
#                     # 1. Create the payload object. This is correct.
#                     request_payload = ChatRequest(request=st.session_state.messages)

#                     # 2. Call the function and receive the SINGLE ChatResponse object.
#                     api_response_object = asyncio.run(chat_endpoint(request_payload))

#                     # 3. Now, unpack the data from the object's attributes.
#                     llm_response = api_response_object.response
#                     source_chunks = api_response_object.source_documents or [] # Use 'or []' for safety

#                     # Display the assistant's response and sources
#                     st.markdown(llm_response)

#                     # Add the complete assistant response to the session state
#                     st.session_state.messages.append({
#                         "role": "assistant",
#                         "message": llm_response,
#                         "sources": source_chunks
#                     })
                    
#                     # Rerun the script to display the new assistant message
#                     st.rerun()

#                 except Exception as e:
#                     error_message = f"An unexpected error occurred: {e}"
#                     st.error(error_message) # st.error will appear on the main page
