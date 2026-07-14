# Day 2: Basic RAG Pipeline

A lightweight Retrieval-Augmented Generation (RAG) pipeline built using LangChain, OpenAI (`gpt-4o-mini`), and Qdrant database.

## Running the Pipeline

1. **Start Qdrant**: `docker compose up -d` at the repository root
2. **Run Ingestion**: `python "basic rag/index.py"` to parse and index the PDF
3. **Run Query**: `python "basic rag/retrieve.py"` to retrieve context and query the LLM
