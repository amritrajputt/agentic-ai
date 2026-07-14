# Day 2: Basic Retrieval-Augmented Generation (RAG) Pipeline

This directory contains a complete, lightweight Retrieval-Augmented Generation (RAG) pipeline built using LangChain, OpenAI, and Qdrant.

## Structure

* **[index.py](file:///d:/google%20collab%20code/day%202/basic%20rag/index.py)**: Handles document ingestion. It loads a local PDF, splits the text into chunks, generates embeddings, and indexes them into a local Qdrant vector database.
* **[retrieve.py](file:///d:/google%20collab%20code/day%202/basic%20rag/retrieve.py)**: Handles query-time retrieval and generation. It connects to the existing Qdrant collection, retrieves relevant context chunks, formats a system prompt, and calls OpenAI's Chat model to answer the query.
* **[DAAUnit3.pdf](file:///d:/google%20collab%20code/day%202/basic%20rag/DAAUnit3.pdf)**: The source PDF document used for indexing.

---

## Features

* **LangChain Integration**: Built with `langchain-qdrant` and `langchain-openai` for seamless integration.
* **Qdrant Vector Database**: Uses Qdrant for storing and searching dense vectors.
* **OpenAI Models**: Utilizes `text-embedding-3-large` for state-of-the-art embedding generation and `gpt-4o-mini` for accurate text generation.
* **Clean Separation of Concerns**: Ingestion and retrieval pipelines are decoupled to avoid parsing the PDF during retrieval requests.

---

## Prerequisites

1. **Docker**: A local Qdrant instance is required. A `docker-compose.yml` is provided at the repository root.
2. **OpenAI API Key**: Set your key in a `.env` file at the root of the repository:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

---

## Setup & Running

### 1. Start Qdrant Services
Run the following command at the repository root to start Qdrant in a Docker container on port `6339`:
```bash
docker compose up -d
```

### 2. Ingestion (Index Documents)
Run `index.py` to parse the PDF, generate embeddings, and populate the Qdrant database:
```bash
python "day 2/basic rag/index.py"
```

### 3. Query & Retrieval
Run `retrieve.py` to retrieve relevant document chunks and generate an answer using the LLM:
```bash
python "day 2/basic rag/retrieve.py"
```
