from langchain_qdrant import QdrantVectorStore
from langchain_openai import ChatOpenAI
from index import embeddings

retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6339",
    collection_name="rag",
    embedding=embeddings
)

query = "write a  where greedy algorithm not works?"
relevent_chunk = retriver.similarity_search(query)

# Extract text content from the retrieved documents
context = "\n\n".join([doc.page_content for doc in relevent_chunk])

SYSTEM_PROMPT = f"""you are a helpful assistant that can answer questions based on the provided context.
context: {context}
"""

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke([
    ("system", SYSTEM_PROMPT),
    ("human", query)
])

print(response.content)
