### User Guide for RAG Application

This application is built using **Streamlit** and **LangChain** to allow users to interact with PDF documents. The user can upload a PDF file, ask questions about its content, and view responses from the system, which are generated using the **GPT** model. Below is a step-by-step guide on how to use the application.

---

### 1. **Uploading a PDF File**

To begin interacting with the application, you need to upload a PDF file that you want to query. Here's how:

- **Step 1**: After launching the app, look for the **sidebar** on the left side of the screen.
- **Step 2**: You will find an option to upload a file. Click on **"Choose a file"** and select a PDF file from your local machine.
  
- **Step 3**: Once the file is uploaded, the system will automatically start processing the PDF.

---

### 2. **Entering Your API Key**

- **Step 1**: If you haven't already set an **OpenAI API Key** as an environment variable, you will be prompted to provide it manually.
  
  - Look for the **API Key input field** on the main page.
  - Enter your API key in the field labeled "OPENAI_API Key" (the input is hidden for security purposes).

- **Step 2**: Once provided, the system will load the PDF file and initialize the chatbot.

---

### 3. **Asking Questions**

After uploading a file and providing your API key, you can begin querying the document. Here's how:

- **Step 1**: In the **chat input** box at the bottom of the screen, type your question. This could be any question related to the content of the PDF you uploaded.


- **Step 2**: Press **Enter** or click **Submit** to send your question.

- **Step 3**: The system will analyze the content of the PDF using a vector-based search and answer your question based on the most relevant sections of the document.

---

### 4. **Viewing Responses**

Once you submit a question, the system generates a response based on the content of the uploaded PDF.

- **Step 1**: The **user's question** will appear in the chat as a message labeled under "user."
- **Step 2**: After a brief wait (shown as a spinner), the system will display an **assistant’s response** below your query.

- **Step 3**: If the context used for generating the response is available, it will also be displayed in the **sidebar** under the "Context" section. You can review the specific text snippets the system used to answer your question.

---

### Key Features

- **Multiple Questions**: You can ask several questions related to the PDF, and the system will keep track of the conversation history to provide context-aware responses.
  
- **Contextual Information**: For each answer, the system displays the relevant portions of the PDF file used to generate the response, providing transparency in the answer generation.

---

### Conclusion

This application leverages OpenAI's GPT and FAISS for question-answering based on PDF content. With easy PDF uploads, seamless API key integration, and intuitive querying, the RAG Application is designed to help users quickly gain insights from large documents. 

Feel free to explore various documents and ask detailed questions to get contextually relevant responses!