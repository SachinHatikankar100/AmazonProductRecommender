import pandas as pd
from langchain_core.documents import Document

class DataLoader:
    def __init__(self,csv_path:str):
        self.csv_path = csv_path

    def convert(self):
        df = pd.read_csv(self.csv_path)[["ProductId","Text"]]

        docs = [
            Document(page_content=row["Text"],metadata={"product id":row["ProductId"]})
            for _,row in df.iterrows()
        ]
        return docs
    
