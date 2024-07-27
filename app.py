import streamlit as st  # for ui
import os
from dotenv import load_dotenv  # to get env variables loaded into the application


# loading of all the env variable
load_dotenv()


# Import the Google generative AI library (assuming this is a hypothetical or internal library)
import google.generativeai as genai


# genai config of api
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# initialise the model
model = genai.GenerativeModel('gemini-pro')


# define a function to generate response from llm
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text


# setting up streamlit app
st.set_page_config(
    page_title="Gemini Pro Q/A Project",
    layout="wide",
    initial_sidebar_state="expanded",
)


# setting up header
st.header("Gemini Q/A App")


# Initialize session state for question history
if 'question_history' not in st.session_state:
    st.session_state.question_history = []


# Input
question = st.text_input("Ask a question:")


# Submit button
if st.button("Submit"):
    if question:
        response = get_gemini_response(question)
        st.write("User:", question)
        st.write("Bot:", response)

        # Add the question to the history
        st.session_state.question_history.append(question)


# Sidebar for question history
st.sidebar.title("📜 Question History")
st.sidebar.markdown("---")  # Add a divider line for better separation


# Display the history with styling
if st.session_state.question_history:
    for i, q in enumerate(st.session_state.question_history, 1):
        st.sidebar.markdown(f"**{i}. {q}**")
else:
    st.sidebar.write("No questions asked yet.")


# Add some extra styling or widgets to the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Stats & More")
st.sidebar.info("Number of questions asked: **{}**".format(len(st.session_state.question_history)))
st.sidebar.success("Keep exploring!")
st.sidebar.markdown("---")


# Optional: Add a reset button to clear the history
if st.sidebar.button("Clear History"):
    st.session_state.question_history = []
    st.sidebar.success("History cleared!")
