from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


pdf_path = Path(__file__).parent / "DAAUnit3.pdf"

loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

spilt_docs = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=os.getenv("OPENAI_API_KEY"))


# vectorstore = QdrantVectorStore.from_documents(
#     documents=spilt_docs,
#     collection_name="rag",
#     url="http://localhost:6339",
#     embedding=embeddings
#     )

print("Documents added to the vector store successfully.ingestion completed.")