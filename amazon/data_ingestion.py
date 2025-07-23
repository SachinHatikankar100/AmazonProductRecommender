from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from amazon.config import config
from amazon.data_loader import DataLoader


class DataIngestion:
    def __init__(self):
        self.embedding = HuggingFaceEndpointEmbeddings(model=config.EMBEDDING_MODEL)

        self.vector_store = AstraDBVectorStore(
            embedding = self.embedding,
            collection_name="AmazonProductRecommender",
            api_endpoint = config.ASTRA_DB_API_ENDPOINT,
            token = config.ASTRA_DB_APPLICATION_TOKEN,
            namespace = config.ASTRA_DB_KEYSPACE
        )


    def ingestion(self,load_existing=True):
        if load_existing==True:
            return self.vector_store
        
        docs = DataLoader("data/Amazon_Reviews.csv").convert()

        self.vector_store.add_documents(docs)
        return self.vector_store



