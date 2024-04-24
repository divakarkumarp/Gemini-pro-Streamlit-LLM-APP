from dotenv import load_dotenv

load_dotenv() ##load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load the Gemini pro model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initialize our streamlit
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM application")

input=st.text_input("Message Google Gemini: ",key="input")
submit=st.button("Ask the question")

#when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("Gemini")
    st.write(response)