from langchain.llms import OpenAI
from constant import openai_api_key as key
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# llm = OpenAI(temperature=0.9)
# prompt = PromptTemplate(
#     input_variables=["product"],
#     template="What is a good name for a company that makes {product}?",
# )
# chain = LLMChain(llm=llm, prompt=prompt)

# # Run the chain only specifying the input variable.
# print(chain.run("colorful socks"))




llm = OpenAI(openai_api_key=key)
prompt=input()
print(llm(prompt))