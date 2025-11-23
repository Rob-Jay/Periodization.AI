from typing import Dict, List
from retriever import retrieve_context
from prompt_builder import build_prompt
from llm_client import query_llm


def run_rag(user_input: Dict) -> str:
    """
    Run the full RAG pipeline:
    1. Retrieve context chunks given the user_input.
    2. Build a prompt combining the user_input and retrieved context.
    3. Query the LLM with that prompt.

    :param user_input: Dict containing user_profile, recent_training, request, weeks, etc.
    :return: Model-generated training plan as a string.
    """
    if "request" not in user_input:
        raise ValueError("user_input must contain a 'request' field for retrieval and prompting.")

    context_chunks: List[str] = retrieve_context(user_input)
    if not context_chunks:
        # You *could* choose to still continue, but it’s usually a sign something is off.
        print("[run_rag] Warning: no context retrieved; continuing with empty context.")

    full_prompt: str = build_prompt(user_input, context_chunks)
    response: str = query_llm(full_prompt)
    return response
