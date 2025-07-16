# streamlit.py (Corrected Version)

import streamlit as st
import asyncio

# These imports are correct
from app.services.chat import chat_endpoint
from app.utils.models import ChatRequest

# --- Page Configuration ---
st.set_page_config(
    page_title="BMA Document Chatbot",
    page_icon="🤖",
    layout="wide"
)

# --- App Title and Description ---
st.title("BMA Document Chatbot")
st.write("แชทบอทสำหรับตอบคำถามเกี่ยวกับระบบ MIS ของกรุงเทพมหานคร")

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message_data in st.session_state.messages:
    with st.chat_message(message_data["role"]):
        st.markdown(message_data["message"])
        if "sources" in message_data and message_data["sources"]:
            with st.expander("View Sources"):
                for i, source in enumerate(message_data["sources"]):
                    st.info(f"Source {i+1}:\n\n---\n\n{source}")

# User Input Handling
if prompt := st.chat_input("พิมพ์คำถามที่ต้องการ..."):
    st.session_state.messages.append({"role": "user", "message": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("กำลังประมวลผล..."):
            try:
                # 1. Create the payload object. This is correct.
                request_payload = ChatRequest(request=st.session_state.messages)

                # 2. Call the function and receive the SINGLE ChatResponse object.
                api_response_object = asyncio.run(chat_endpoint(request_payload))

                # 3. Now, unpack the data from the object's attributes.
                llm_response = api_response_object.response
                source_chunks = api_response_object.source_documents or [] # Use 'or []' for safety

                # Display the assistant's response and sources
                st.markdown(llm_response)

                if source_chunks:
                    with st.expander("View Sources"):
                        for i, source in enumerate(source_chunks):
                            st.info(f"Source {i+1}:\n\n---\n\n{source}".replace("#", ""))

                # Add the complete assistant response to the session state
                st.session_state.messages.append({
                    "role": "assistant",
                    "message": llm_response,
                    "sources": source_chunks
                })

            except Exception as e:
                error_message = f"An unexpected error occurred: {e}"
                st.error(error_message)