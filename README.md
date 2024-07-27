# AI-Chat-Bot

## Overview
This project implements a chatbot using the Gemini Pro API, allowing users to interact with a large language model. The chatbot is designed to respond to user queries in a natural and coherent manner. The frontend is built using Streamlit.

## Introduction
The GenAI ChatBot is designed to leverage the power of Google's Gemini API to provide intelligent and context-aware responses. By integrating with streamlit, the ChatBot offers a user-friendly interface that allows seamless interaction with users.

## Installed modules 
streamlit
os
python-dotenv
google-generativeai

## Features
Natural Language Processing: Utilizes Google Gemini API for understanding and generating human-like responses.
Interactive Interface: Built with streamlit for a responsive and user-friendly experience.
Environment Configuration: Uses python-dotenv for managing environment variables securely.


## Installation

**Clone the Repository**
   ```bash
   git clone <https://github.com/MuktiMishra/GeminiGizmo.git>
   cd <repository-directory>

**Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

**Install Dependencies**
   ```bash
   pip install -r requirements.txt
 
**Set Up Environment Variables**
    Create a .env file in the project root directory.
    Add your Gemini Pro API key to the .env file:
    GEMINI_API_KEY=your_api_key_here

## Usage
 
1. **Run the Streamlit App**
    ```bash
    streamlit run app.py

2. **Interact with the Chatbot**
   Open your web browser and go to http://localhost:8501/
   Type your question in the input field and click "Submit" to get a response from the chatbot.



