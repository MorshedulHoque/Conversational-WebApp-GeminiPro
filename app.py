from dotenv import load_dotenv
load_dotenv()   #loading all the environment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-pro")

# function to get gemini pro model and response
def get_gemini_response(question):
    response = model.generate_content(question)
    
    return response.text



#initialize streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemnini LLM Application")

input = st.text_input("Input: ", key=input)
submit = st.button("Ask the question")

#When submit is click

if submit:
    response = get_gemini_response(input)
    st.write(response)