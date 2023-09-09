import os
import streamlit as st
from  constant import openai_api_key
from langchain.llms import OpenAI


os.environ["OPENAI_API_KEY"]=openai_api_key

st.title("Search Text")
input_text=st.text_input("Search topic")

llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text)) 