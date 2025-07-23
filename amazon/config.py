import os
from dotenv import load_dotenv

load_dotenv()

class config:
    GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
    ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")
    EMBEDDING_MODEL="BAAI/bge-base-en-v1.5"
    RAG_MODEL="models/gemini-2.5-flash"