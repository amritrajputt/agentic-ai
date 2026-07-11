# Agentic AI - Text Generation Pipeline

This repository contains a simple, robust, and device-agnostic text generation pipeline using Hugging Face's Transformers library and Google's **Gemma-3-1b-it** model.

## Features

- **Device Agnostic**: Automatically detects and utilizes GPU (`cuda`) for acceleration, falling back gracefully to CPU if not available.
- **Optimized Data Types**: Uses `float16` precision on GPU for faster inference and lower memory usage, and `float32` on CPU to prevent runtime issues.
- **Secure Secret Management**: Integrates with Google Colab's built-in secrets manager and standard environment variables to prevent accidental API key leaks.

## Project Structure

- `day 1/`
  - [pipeline.py](file:///d:/google%20collab%20code/day%201/pipeline.py): The main script that loads the model, tokenizes the input, runs inference, and decodes the output.
- [.gitignore](file:///d:/google%20collab%20code/.gitignore): Ignores local compilation caches and secret files.

## Prerequisites

To run this pipeline, you need a Hugging Face account and an access token to load the Gemma model.

### 1. Request access to Gemma 3
Go to the Hugging Face page for [google/gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) and accept the license terms.

### 2. Generate a Hugging Face Token
Create a read access token in your Hugging Face account under **Settings > Access Tokens**.

---

## How to Run

### Option A: In Google Colab (Recommended)

1. Open your notebook in Google Colab.
2. In the left-hand sidebar, click the **Secrets** (key icon 🔑) tab.
3. Add a new secret with:
   - **Name**: `HF_TOKEN`
   - **Value**: *Your Hugging Face token*
4. Enable **Notebook access** for the secret.
5. Install the required dependencies:
   ```bash
   pip install transformers torch accelerate
   ```
6. Run the script!

### Option B: Running Locally

1. Install the required libraries:
   ```bash
   pip install transformers torch accelerate
   ```
2. Set your Hugging Face Token as an environment variable in your terminal:
   - **Windows (PowerShell)**:
     ```powershell
     $env:HF_TOKEN="your_token_here"
     ```
   - **Windows (CMD)**:
     ```cmd
     set HF_TOKEN=your_token_here
     ```
   - **Linux/macOS**:
     ```bash
     export HF_TOKEN="your_token_here"
     ```
3. Execute the pipeline:
   ```bash
   python "day 1/pipeline.py"
   ```
