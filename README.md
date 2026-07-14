# Agentic AI & Machine Learning Experiments

Welcome to the **Agentic AI & Machine Learning Experiments** repository! This is a general-purpose space dedicated to daily learnings, experimental code, and implementations of modern AI pipelines, Agentic workflows, and Deep Learning models.

## Repository Structure

As the repository grows, content will be organized by daily topics or features:

* **[day 1/](file:///d:/google%20collab%20code/day%201)**: Text Generation Pipeline using Google's `gemma-3-1b-it`.
* **[day 2/](file:///d:/google%20collab%20code/day%202)**: Basic Retrieval-Augmented Generation (RAG) Pipeline using LangChain, Qdrant, and OpenAI.

---

## Contents

### Day 1: Text Generation Pipeline
Located in [day 1/pipeline.py](file:///d:/google%20collab%20code/day%201/pipeline.py), this project implements a simple, robust, and device-agnostic text generation pipeline using Hugging Face's Transformers library.

#### Features
* **Device Agnostic**: Automatically detects and utilizes GPU (`cuda`) for acceleration, falling back gracefully to CPU if not available.
* **Optimized Data Types**: Uses `float16` precision on GPU for faster inference and lower memory usage, and `float32` on CPU to prevent runtime issues.
* **Secure Secret Management**: Integrates with Google Colab's built-in secrets manager and standard environment variables to prevent accidental API key leaks.

#### Prerequisites
To run this pipeline, you need a Hugging Face account and an access token to load the Gemma model.
1. Request access to Gemma 3 on the Hugging Face page for [google/gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it).
2. Generate a read access token in your Hugging Face account under **Settings > Access Tokens**.

#### Setup & Execution

##### Option A: In Google Colab (Recommended)
1. In the left-hand sidebar of Google Colab, click the **Secrets** (key icon 🔑) tab.
2. Add a new secret with the name `HF_TOKEN` and your token as the value, and enable **Notebook access**.
3. Install dependencies and run the script:
   ```bash
   pip install transformers torch accelerate
   ```

##### Option B: Running Locally
1. Install dependencies:
   ```bash
   pip install transformers torch accelerate
   ```
2. Set the `HF_TOKEN` environment variable in your terminal:
   * **Windows (PowerShell)**: `$env:HF_TOKEN="your_token_here"`
   * **Windows (CMD)**: `set HF_TOKEN=your_token_here`
   * **Linux/macOS**: `export HF_TOKEN="your_token_here"`
3. Execute the pipeline:
   ```bash
   python "day 1/pipeline.py"
   ```

### Day 2: Basic RAG Pipeline
Located in [day 2/](file:///d:/google%20collab%20code/day%202), this implements a document ingestion and retrieval pipeline using LangChain, OpenAI (`gpt-4o-mini`), and Qdrant.
