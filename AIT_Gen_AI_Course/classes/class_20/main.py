from dotenv import load_dotenv
load_dotenv()  # SABSE PEHLE

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeEmbeddings
from langchain_pinecone import PineconeVectorStore

from rag1 import md_header_splits

import time
import os

model_name = 'multilingual-e5-large'
embeddings = PineconeEmbeddings(
    model=model_name,
    pinecone_api_key=os.environ.get('PINECONE_API_KEY')
)

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

cloud = os.environ.get('PINECONE_CLOUD') or 'aws'
region = os.environ.get('PINECONE_REGION') or 'us-east-1'
spec = ServerlessSpec(cloud=cloud, region=region)

index_name = "rag-getting-started"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=embeddings.dimension,
        metric="cosine",
        spec=spec
    )

# See that it is empty
print("Index before upsert:")
print(pc.Index(index_name).describe_index_stats())
print("\n")

namespace = "wondervector5000"

docsearch = PineconeVectorStore.from_documents(
    documents=md_header_splits,
    index_name=index_name,
    embedding=embeddings,
    namespace=namespace
)

time.sleep(5)

# See how many vectors have been upserted
print("Index after upsert:")
print(pc.Index(index_name).describe_index_stats())
print("\n")
time.sleep(2)

index = pc.Index(index_name)
namespace = "wondervector5000"

for ids in index.list(namespace=namespace):
    query = index.query(
        id=ids[0], 
        namespace=namespace, 
        top_k=1,
        include_values=True,
        include_metadata=True
    )
    print(query)
    print("\n")