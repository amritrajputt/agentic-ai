import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set Hugging Face token securely
# - In Google Colab: Set HF_TOKEN in the "Secrets" tab (key icon on the left panel) and enable Notebook access.
# - In local environments: Set the HF_TOKEN environment variable in your shell/system.
if "HF_TOKEN" not in os.environ:
    try:
        from google.colab import userdata
        token = userdata.get("HF_TOKEN")
        if token:
            os.environ["HF_TOKEN"] = token
    except ImportError:
        pass 

# Define the model to use
model_name = "google/gemma-3-1b-it"

# Check if GPU is available (strongly recommended for float16 models)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define the prompt (this was missing/undefined)
input_prompt = "Explain quantum computing in simple terms."

# Tokenize the input and move the tensor to the device
tokenized = tokenizer(input_prompt, return_tensors="pt").to(device)

# Load the model (use float16 on GPU, float32 on CPU)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
).to(device)

# Generate text
gen_result = model.generate(
    tokenized["input_ids"], 
    attention_mask=tokenized.get("attention_mask"), 
    max_new_tokens=25
)
print("Generated token IDs:", gen_result)

# Decode and print output
output = tokenizer.batch_decode(gen_result, skip_special_tokens=True)
print("Decoded output:")
print(output[0])