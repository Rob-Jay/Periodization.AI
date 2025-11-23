# rag_engine/llm_client.py  (Local generation via Ollama)
# Requires: Ollama running locally and a pulled model (e.g., `ollama pull mistral`)
# If `ChatOllama` import fails, install: `pip install langchain-ollama`
from typing import List
from langchain_community.chat_models import ChatOllama
from langchain.schema import SystemMessage, HumanMessage

def query_llm(prompt: str) -> str:
    chat = ChatOllama(
        model="mistral",       # alternatives: "llama3", "llama3.1", "qwen2"
        temperature=0.2,
        # base_url="http://localhost:11434"  # default; set if custom
    )
    messages: List = [
        SystemMessage(content="You are a training coach. Be concise, evidence-aware, and structured."),
        HumanMessage(content=prompt),
    ]
    res = chat.invoke(messages)
    return res.content.strip()