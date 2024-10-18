import PyPDF2
import os
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

class RAGChain:
    def __init__(self, pdf_file_path, api_key=os.getenv("OPENAI_API_KEY")):
        pdf_text = self.extract_text_from_pdf_with_pypdf2(pdf_file_path)
        chunked_documents = self.create_chunks_for_pypdf2_parse(pdf_text)
        vectorstore = self.create_vectorstore_with_faiss(chunked_documents)
        # Creating LLM
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)
        # Creating Retriever from vectorstore
        self.retriever = vectorstore.as_retriever()
        # Create a chat history to store the conversation history
        self.chat_history = []
    
    def ask_question(self, question):
        # Create a chat history text to pass to LLM to create a single question
        chat_history_text = "\n".join([f"User:{f['user']}\nAssistant:{f['assistant']}" for f in self.chat_history[:-10]])
        # Prompt to create a single question that will help us retrieve relevant context
        single_question_prompt = f"You will be given chat history and the user question. Your task is to reply with a single question that accurately represents the user question based on the context of the chat history. \n\nChat history:\n{chat_history_text}\n\nUser question: {question}\n\n Reply with the single question and nothing else.\n\nSingle Answer:"
        # Use LLM to create a single question
        single_question = self.llm.invoke(single_question_prompt).content
        # Retrieve the relevant context from the vectorstore
        context = self.retriever.invoke(single_question)
        context = [f.page_content for f in context]
        context_text = "\n\n".join(context)
        # Prompt to answer the single question
        answer_prompt = f"You will be given a context and a question. Your task is to answer the question based on the context. \n\nContext:\n{context_text}\n\nQuestion: {single_question}\n\n Answer:"
        # Use LLM to answer the question
        answer = self.llm.invoke(answer_prompt).content
        # Update the chat history
        self.chat_history.append({"user": question, "assistant": answer})
        # Return the answer
        return answer, context

    def clear_history(self):
        self.chat_history = []

    def get_chat_history(self):
        return self.chat_history
    
    def extract_text_from_pdf_with_pypdf2(self, file_path):
        pdf_reader = PyPDF2.PdfReader(file_path)
        
        full_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            full_text += text + "\n"
        
        return full_text

    def create_chunks_for_pypdf2_parse(self, pdf_text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        chunks = text_splitter.split_text(pdf_text)
        return chunks

    def create_vectorstore_with_faiss(self, chunked_documents):
        embedding_function = OpenAIEmbeddings()
        if type(chunked_documents[0]) == str:
            vectorstore = FAISS.from_texts(chunked_documents, embedding_function)
        else:
            vectorstore = FAISS.from_documents(chunked_documents, embedding_function)
        # Save the vectorstore to local path
        return vectorstore
