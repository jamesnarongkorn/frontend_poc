import streamlit as st
import json
import asyncio # <-- Import asyncio

# Import the logic function and the separator constant
from app.services.chat_poc import get_chat_response, SOURCES_SEPARATOR

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
        <img src="https://officialadmin.bangkok.go.th/Admin/images/logo.png" width="60" style="margin-right: 15px;">
    </div>
    <p>แชทบอทสำหรับตอบคำถามเกี่ยวกับระบบ MIS ของกรุงเทพมหานคร</p>
    """,
    unsafe_allow_html=True
)

# Configuration
use_streaming = st.toggle("Enable Streaming Response", value=True)

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Create a container for the chat history
chat_container = st.container(border=True)

# Display Chat History from session state
with chat_container:
    for message_data in st.session_state.messages:
        with st.chat_message(message_data["role"]):
            st.markdown(message_data["message"])
            if "sources" in message_data and message_data["sources"]:
                with st.expander("View Sources"):
                    for i, source in enumerate(message_data["sources"]):
                        source_text = str(source).replace("#", "")
                        st.info(f"Source {i+1}:\n\n---\n\n{source_text}")

# --- User Input Handling ---
if prompt := st.chat_input("พิมพ์คำถามที่ต้องการ..."):
    st.session_state.messages.append({"role": "user", "message": prompt})
    st.rerun()

# --- Generate and Display Assistant Response ---
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    with chat_container:
        with st.chat_message("assistant"):

            # --- Streaming Logic ---
            if use_streaming:
                message_placeholder = st.empty()
                
                try:
                    # This async function will now return the final results
                    async def stream_and_display():
                        # Define variables locally within the async function
                        local_full_response = ""
                        local_sources = []
                        local_header_buffer = ""
                        local_header_found = False

                        async_generator = await get_chat_response(
                            messages=st.session_state.messages,
                            streaming=True
                        )

                        async for chunk in async_generator:
                            if not local_header_found:
                                local_header_buffer += chunk
                                separator_with_newline = SOURCES_SEPARATOR + '\n'
                                
                                if separator_with_newline in local_header_buffer:
                                    local_header_found = True
                                    header_part, initial_text_chunk = local_header_buffer.split(separator_with_newline, 1)
                                    
                                    try:
                                        local_sources = json.loads(header_part)
                                    except json.JSONDecodeError:
                                        st.warning("Could not parse sources from the stream.")
                                        local_full_response += local_header_buffer
                                    else:
                                        local_full_response += initial_text_chunk
                                    
                                    message_placeholder.markdown(local_full_response + "▌")
                            else:
                                local_full_response += chunk
                                message_placeholder.markdown(local_full_response + "▌")

                        if not local_header_found:
                            local_full_response = local_header_buffer
                        
                        # Return the final state of the variables
                        return local_full_response, local_sources

                    # Run the async function and capture the returned values
                    full_response, sources = asyncio.run(stream_and_display())

                    # Final update after the stream is complete
                    message_placeholder.markdown(full_response)
                    
                    if sources:
                        with st.expander("View Sources", expanded=False):
                            for i, source in enumerate(sources):
                                source_text = str(source).replace("#", "")
                                st.info(f"Source {i+1}:\n\n---\n\n{source_text}")
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "message": full_response,
                        "sources": sources 
                    })

                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")

            # --- Non-Streaming Logic ---
            else:
                with st.spinner("Thinking..."):
                    try:
                        response_data = asyncio.run(get_chat_response(
                            messages=st.session_state.messages,
                            streaming=False
                        ))
                        
                        llm_response = response_data.get("response", "Sorry, I couldn't get a response.")
                        source_chunks = response_data.get("sources", [])

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
