import os
import streamlit as st
from  constant import openai_api_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

os.environ["OPENAI_API_KEY"]=openai_api_key

st.title("Search People")
input_text=st.text_input("Search topic")

#Prompt
first_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name}",
)

#Memory
person_memory=ConversationBufferMemory(input_key='name', memory_key='chat-history')
dob_memory=ConversationBufferMemory(input_key='person', memory_key='chat-history')
desc_memory=ConversationBufferMemory(input_key='dob', memory_key='chat-history')



llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm, prompt=first_prompt, verbose=True, output_key='person', memory=person_memory )


second_prompt=PromptTemplate(
    input_variables=['person'],
    template="when was  {person} born",
)


chain2=LLMChain(llm=llm, prompt=second_prompt, verbose=True, output_key='dob', memory=dob_memory )

third_prompt=PromptTemplate(
    input_variables=['dob'],
    template="what are other events happened  on  {dob} in india  ",
)
chain3=LLMChain(llm=llm, prompt=third_prompt, verbose=True, output_key='description' , memory=desc_memory)



parent_chain=SequentialChain(chains=[chain, chain2, chain3], 
                             input_variables=['name'],
                               output_variables=['person','dob', 'description'],
                               verbose=True)

if input_text:
    st.write(parent_chain({'name':input_text}))   
    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Description'):
        st.info(desc_memory.buffer)