import streamlit as st
from ollama import chat

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit app title
st.title("Interactive Chat with Ollama LLM")

# CSS for styling chat bubbles
st.markdown(
    """
    <style>
    .user-message {
        background-color: #B52F2F;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        color: white;
    }
    .assistant-message {
        background-color: #3BA211;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.success("Chat history cleared!")

# Display the chat history
st.subheader("Chat History")
if st.session_state.messages:
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.markdown(
                f"<div class='user-message'>You: {message['content']}</div>", 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='assistant-message'>LLM: {message['content']}</div>", 
                unsafe_allow_html=True
            )

# User input box
user_input = st.text_input("Enter your message:")
txt = user_input

# Button to send the message
if st.button("Send"):
    if user_input.strip():  # Only proceed if the input is not empty
        # Add the user message to chat history
        st.session_state.messages.append({"role": "user", "content": txt})

        # Display a loading spinner
        with st.spinner("Fetching response..."):
            try:
                # Stream response from Ollama
                stream = chat(
                    model='llama3.2:1b',
                    messages=st.session_state.messages,
                    stream=True
                )
                response_content = ""
                # Create a placeholder for streaming
                response_placeholder = st.empty()
                for chunk in stream:
                    response_content += chunk['message']['content']
                    # Update the placeholder with the streaming response
                    response_placeholder.markdown(
                        f"<div class='assistant-message'>LLM:{response_content}</div>", 
                        unsafe_allow_html=True
                    )

                # Add the final response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response_content})

                # Clear the user input box
                st.session_state.user_input = ""
            except Exception as e:
                st.error(f"An error occurred: {e}")
