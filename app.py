import os
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

st.title("RAG-enabled Groq Chatbot")

@st.cache_resource
def load_and_process_documents():
    directory = "data/"
    all_documents = []
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            loader = TextLoader(file_path)
            documents = loader.load()
            all_documents.extend(documents)
            count += 1
    
    st.write(f"Total number of text files added: {count}")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    text_chunks = text_splitter.split_documents(all_documents)
    st.write(f"Added {len(text_chunks)} chunks to the Chroma database.")
    
    persist_directory = "clg_db"
    embedding = HuggingFaceEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=text_chunks,
        embedding=embedding,
        persist_directory=persist_directory
    )
    
    return vectorstore

vectorstore = load_and_process_documents()

retriever = vectorstore.as_retriever()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Generating response..."):
        response = qa_chain.invoke({"query": prompt})

    with st.chat_message("assistant"):
        st.markdown(response["result"])
    st.session_state.messages.append({"role": "assistant", "content": response["result"]})

    with st.expander("View Source Documents"):
        for doc in response["source_documents"]:
            st.write(doc.page_content)
            st.write(f"Source: {doc.metadata.get('source', 'Unknown')}")
            st.write("---")

st.sidebar.title("About")
st.sidebar.info("This is a RAG-enabled chatbot using Groq and Langchain. It answers questions based on the loaded text documents.")
st.sidebar.write("Model: llama-3.1-8b-instant")
