# Interactive Chat with Ollama LLM

## Overview

This Streamlit-based application provides an interactive chat interface with the Ollama Large Language Model (LLM). It allows users to input messages, receive real-time responses from the model, and view the chat history with a visually appealing design.

---

## Features

- **Real-time Chat**: Communicate with the Ollama LLM in a responsive and dynamic chat interface.  
- **Styled Chat Bubbles**: Messages from the user and LLM are displayed in distinct, color-coded chat bubbles for better readability.  
- **Streamed Responses**: LLM responses are streamed to provide a smooth conversational experience.  
- **Chat History Management**: View the complete chat history or clear it with a single click.  

---

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.8+**
- **Streamlit**: Install via `pip install streamlit`.  
- **Ollama SDK**: Install via `pip install ollama`.  
- **Ollama Model**: Ensure access to the `llama3.2:1b` model used in this application.  

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/srishrachamalla7/ollama_chatbot.git
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the Application**
   Open your web browser and navigate to `http://localhost:8501`.

---

## How It Works

1. **Chat Initialization**: The application initializes chat history in the session state.  
2. **User Interaction**:  
   - Users can type messages in the input box and click the **Send** button.  
   - The message is added to the chat history and sent to the Ollama LLM.  
3. **Streaming Responses**:  
   - The response from the LLM is streamed in real-time and displayed in the chat interface.  
4. **Chat Management**:  
   - Users can clear the chat history using the **Clear Chat** button.

---

## Demo

![ollama_demeo_chabot](https://github.com/user-attachments/assets/015cc7d2-de8a-4860-b3c3-1b501417376a)


## Troubleshooting

- **Connection Issues**: Ensure that the Ollama SDK is correctly installed and configured.  
- **Model Access**: Verify access to the `llama3.2:1b` model.  
- **Streamlit Errors**: Check for any environment-specific issues and ensure all dependencies are installed.  

---

## Disclaimer

This application is intended for educational purposes. Ensure compliance with the terms of use of the Ollama SDK and associated models.
