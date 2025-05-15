import os
from dbm import error
from warnings import catch_warnings

from click import prompt
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM
from langchain_weaviate.vectorstores import WeaviateVectorStore
# from langchain_core.retrievers import BaseRetriever
# from loader import get_weaviate_client,get_embeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from sqlalchemy import except_

from utils.loader import get_embeddings

load_dotenv()

def get_llm():
    return WatsonxLLM(
        model_id=os.getenv("WATSONX_LLM_MODEL"),
        url=os.getenv("WATSONX_URL"),
        apikey=os.getenv("WATSONX_API_KEY"),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        params={
            "max_new_tokens":200
        }
    )

def get_retriever(vectorstore):
    try:
        retriever = vectorstore.as_retriever( # Enables Max Marginal Relevance
            search_kwargs={
                "k":5
            }
        )
        return retriever
    except Exception as e:
        return e

def create_rag_pipe(vectorstore,suffix):
    retriever = get_retriever(vectorstore)
    llm=get_llm()

    print(retriever)

    if suffix in ['.xlsx','.xlx','.csv']:
        prompt_text ="""You are currently acting as a financial analyst assistant. Use the following context:
                        {context}
                        
                        For questions related to spreadsheets, please adhere to these guidelines:
                        - Always reference exact numbers from tables.
                        - Compare values across different periods (quarters, years, etc.).
                        - Identify and describe any trends present in the data.
                        - for relevant data information try to create a table
                        - If currency values are mentioned, always specify the currency.
                        
                        Question: {question}
                        Answer:"""
    else:
        prompt_text="""You are a knowledgeable assistant designed to answer questions using only the information retrieved from the provided document. Read the context carefully and answer the question based strictly on the content.

        Context:
        {context}
        
        Guidelines:
        - Understand what the question is specifically asking.
        - first introduce the premise of the question in the first paragraph precisely.
        - Use only the facts and details available in the context.
        - If the answer involves numbers, dates, definitions, or references, mention them exactly as presented.
        - If the answer is not clearly stated in the context, respond with: "The answer is not available in the provided document."
        - Answer in a well structured format into paragraphs differentiating each concept of the answer.
        - if there are headings to the answer bold them and if posible while differentiating use tables.
        
        Question: {question}
        Answer:        
        """

    prompt = ChatPromptTemplate.from_template(prompt_text)

    return (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
    )

def query_rag_pipe(question: str, rag_pipe):
    return rag_pipe.invoke(question)
