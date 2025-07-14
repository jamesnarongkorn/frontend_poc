import streamlit as st
import requests
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="BMA Document Chatbot",
    page_icon="🤖",
    layout="wide"
)

# --- App Title and Description ---
st.title("BMA Document Chatbot 🤖")
st.write("Ask questions about your documents, and this bot will answer based on the provided knowledge base.")

# --- Configuration ---
# This is the URL where your FastAPI backend is running.
# Make sure the port number matches the one you are using for `uvicorn`.
FASTAPI_URL = "http://127.0.0.1:8000/api/v1/chat"

# --- Session State Initialization ---
# This will now store the history in the format: [{"role": "user", "message": "..."}]
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Chat History ---
# Loop through the stored messages and display them.
for message_data in st.session_state.messages:
    # `message_data` is a dict like {"role": "...", "message": "...", "sources": [...]}
    with st.chat_message(message_data["role"]):
        st.markdown(message_data["message"])
        # If the message is from the assistant and has sources, display them
        if "sources" in message_data and message_data["sources"]:
            with st.expander("View Sources"):
                for i, source in enumerate(message_data["sources"]):
                    st.info(f"Source {i+1}:\n\n---\n\n{source}")

# --- User Input Handling ---
if prompt := st.chat_input("Ask your question here..."):
    # 1. Add user's message to session state and display it
    # CHANGED: Storing with the 'message' key to match the API
    st.session_state.messages.append({"role": "user", "message": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Prepare to display the assistant's response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # 3. CHANGED: Construct the new request body
                # The backend will likely ignore the 'sources' key for assistant messages, which is fine.
                api_request_payload = {
                    "request": st.session_state.messages,
                }

                # 4. Call the FastAPI backend with the new payload
                response = requests.post(FASTAPI_URL, json=api_request_payload)
                response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)

                # 5. Parse the response
                data = response.json()
                llm_response = data.get("response", "Sorry, I couldn't get a response.")
                source_chunks = data.get("source_documents", [])

                # 6. Display the assistant's response and sources
                st.markdown(llm_response)

                if source_chunks:
                    with st.expander("View Sources"):
                        for i, source in enumerate(source_chunks):
                            st.info(f"Source {i+1}:\n\n---\n\n{source}".replace("#", ""))

                # 7. CHANGED: Add the complete assistant response to the session state
                # using the new 'message' key format.
                st.session_state.messages.append({
                    "role": "assistant",
                    "message": llm_response,
                    "sources": source_chunks
                })

            except requests.exceptions.RequestException as e:
                error_message = f"Could not connect to the backend API. Please ensure it is running at {FASTAPI_URL}. Error: {e}"
                st.error(error_message)
                # No need to add this error to chat history again
            except Exception as e:
                error_message = f"An unexpected error occurred: {e}"
                st.error(error_message)
