import streamlit as st
from amazon.rag_chain import RAGBuilder
from dotenv import load_dotenv
from amazon.data_ingestion import DataIngestion

st.set_page_config(page_title="Amzon Product Recommender", layout="wide")
load_dotenv()


@st.cache_resource
def init_pipeline():
    return RAGBuilder(vector_store=DataIngestion().ingestion())

pipeline = init_pipeline()


st.title("Amazon Product Recommender")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me about products..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            rag_chain = pipeline.build_rag_chain()
            clean_prompt = str(prompt).strip() if prompt else ""
            response = rag_chain.invoke({"input": clean_prompt}, config={"configurable": {"session_id": "user"}})
            
            bot_response = response["answer"]
            st.markdown(bot_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # In sidebar 
with st.sidebar:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()