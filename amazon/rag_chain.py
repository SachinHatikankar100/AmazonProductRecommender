from langchain_core.chat_history import BaseChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from amazon.config import config
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_history_aware_retriever,create_retrieval_chain
from langchain_community.chat_message_histories import ChatMessageHistory



class RAGBuilder:
    def __init__(self,vector_store):
        self.vector_store = vector_store
        self.model = ChatGoogleGenerativeAI(model=config.RAG_MODEL,temperature=0.5)
        self.history={}

    def _get_history(self,session_id:str)-> BaseChatMessageHistory:
        if session_id not in self.history:
            self.history[session_id]=ChatMessageHistory()
        return self.history[session_id]
    
    def build_rag_chain(self):

        retriever = self.vector_store.as_retriever(search_kwargs={"k":3})

        context_prompt = ChatPromptTemplate.from_messages([
            ("system", "Given the chat history and user question, rewrite it as a standalone question."),
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human","{input}")
        ])

        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", """You're an e-commerce bot answering product-related queries using reviews and titles.
                          Stick to context. Be concise and helpful.\n\nCONTEXT:\n{context}\n\nQUESTION: {input}"""),
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human","{input}")
        ])


        history_aware_retriever = create_history_aware_retriever(
            self.model,retriever,context_prompt
        )

        qa_chain = create_stuff_documents_chain(
            self.model,qa_prompt
        )

        rag_chain = create_retrieval_chain(
            history_aware_retriever,qa_chain
        )

        return RunnableWithMessageHistory(
            rag_chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )