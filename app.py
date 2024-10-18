import streamlit as st
import os
import tempfile

from dotenv import load_dotenv
load_dotenv()

from streamlit_functions import RAGChain
def main():
    st.title("RAG Application")
    
    if "openai_api_key" not in st.session_state:
        st.session_state.openai_api_key = os.getenv("OPENAI_API_KEY")
    if "RAGChatbot" not in st.session_state:
        st.session_state.RAGChatbot = None

    if st.session_state.openai_api_key is None:
        st.session_state.openai_api_key = st.text_input("OPENAI_API Key", type="password")
    else:
        with st.sidebar:
            if uploaded_file := st.file_uploader("Choose a file", type=["pdf"]):
                with tempfile.TemporaryDirectory() as tmpdirname:
                    with open(os.path.join(tmpdirname, uploaded_file.name), "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    st.session_state.RAGChatbot = RAGChain(pdf_file_path=os.path.join(tmpdirname, uploaded_file.name), api_key=st.session_state.openai_api_key)

    if st.session_state.RAGChatbot is not None:
        for chat_message in st.session_state.RAGChatbot.get_chat_history():
            with st.chat_message("user"):
                st.write(chat_message["user"])
            with st.chat_message("assistant"):
                st.write(chat_message["assistant"])
        if user_query := st.chat_input("Ask a question:"):
            with st.chat_message("user"):
                st.write(user_query)
            with st.spinner("Waiting for response..."):
                answer, context_list = st.session_state.RAGChatbot.ask_question(user_query)
            with st.chat_message("assistant"):
                st.write(answer)
            with st.sidebar:
                st.subheader("Context")
                for context in context_list:
                    st.write(context)
                    st.write("-"*25)

if __name__ == "__main__":
    main()