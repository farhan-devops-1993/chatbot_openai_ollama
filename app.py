from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set env variables (optional, usually not needed after load_dotenv). we will assign the variables, call the environemnt variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") #now, for langsmith tracking we will use langsmith api call

# Enable Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"


#now, we will create the chatbot. Creating chatbot
#1- Firslt we will create our prompt. it will tell the model what to do. and we will create two tuples.1- system, 2- human
prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant, please provide the response to the user queries."),
    ("user", "Question:{question}")
])

#so, here we will have the combination of three. like firstly, we will create the ChatpromptTemplate, then we will create the ChatOpenAI, and then the result of ChatOpenAI will be passed to StrOutputParser

#streamlit framework , we will create the chatbot interface
st.title("Langchain Demo with OpenAI API") #this will create the title of the chatbot
input_text=st.text_input("Search teh Topic you want") #this will create the text input field

#OpenAI LLM call
llm=ChatOpenAI(temperature=0.7) #this will create the OpenAI LLM call
#after that, what llm model will get the response, it will display with respect to the StrOutputParser
output_parser=StrOutputParser() #this will create the StrOutputParser, and display in string format.


#Create Chain, what is chain? like we already discussed, at frist our chat prompt is ready, then it will interact the chatopenai OpenAI LLM call, and then it will display the response with respect to the StrOutputParser
#we will create teh chain in this same format
chain=prompt | llm | output_parser #this is chain one by one, like we are using or operator. this chain will be responsive to the user input

if input_text:
    st.write(chain.invoke({"question": input_text})) #this will display the response

#now, let's understand the flow of the chatbot, we give input_text to the chain, chain invoke and then it will interact with the  prompt and that input will assign to Question and then goto LLM Model, Model will give the response and outputparser will parse the response and display in string format.