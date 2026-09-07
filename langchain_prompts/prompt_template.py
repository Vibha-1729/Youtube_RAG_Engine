from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
load_dotenv()

model=GoogleGenerativeAI(model='gemini-3.6-flash')
st.header('Research Tool')

paper_input=st.selectbox()
style_input=st.selectbox()
length_input=st.selectbox()

if(st.button('Summarize')):
    st.write("Hello")
