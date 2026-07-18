from langchain_pinecone import PineconeEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

pinecone_key = os.environ.get("PINECONE_API_KEY")

model_name = 'multilingual-e5-large'
embeddings = PineconeEmbeddings(
    model=model_name,
    pinecone_api_key=pinecone_key
)

print(PineconeEmbeddings.pinecone_api_key)