from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

promt=ChatPromptTemplate.from_messages(
    [("system","you are a helpful assistant. please respond to the queries."),
     ("user","Question:{question}")
     ]
)
st.title("langchain demo with openai")
input_text=st.text_input("search the topic you want")

llm=ChatOpenAI(model='gpt-3.5-turbo',temperature=0)
output_parser=StrOutputParser()
chain=promt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))
    
