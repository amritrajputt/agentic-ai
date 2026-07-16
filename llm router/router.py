import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()  
client  = Groq(api_key=os.environ.get("GROQ_API_KEY"))

MODEL_CATALOG = """
- gpt-5.5 — strongest agentic/tool-use, broad ecosystem, verbose on long-form, pricier
- claude-opus-4-8 — best coding/long-form writing, most expensive, slower
- claude-sonnet-4-6 — near-Opus quality, moderate cost, good default for app-building
- claude-haiku-4-5 — very cheap/fast, good for simple classification/summaries, weak on deep reasoning
- gemini-3-1-pro — huge context window, fast throughput, strong reasoning, weaker creative consistency
- gemini-flash-lite — cheapest, fastest, good for high-volume simple/multimodal tasks, low reasoning depth
- deepseek-v4 — best cost-to-performance, near-frontier coding/reasoning, hallucination risk on facts
- grok-4-3 — real-time X/web search, weaker coding, expensive top tier
- llama-4 — free self-hosted, full data control, trails frontier on peak reasoning
"""

SYSTEM_PROMPT = f""" you are a model router that can route queries to the best model based on the user's query. 
pick the best model from the following catalog based on the user's query.also take care of the cost of the model.
make a balanced decision between the models based on the user's query and price.

Available models:{MODEL_CATALOG}

Rules: 
1. Analyze the user's query ,reasoning depth needed and where the high cost is justified.
2. do not default to any model.
3. output the model id string . no explanation needed. no punctuation needed."""


def route_query(query:str)->str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    query = "i want to know which model is best to talk rudely"
    print(route_query(query))