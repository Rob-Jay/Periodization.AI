# rag_engine/retriever.py  (HuggingFace embeddings version – must match ingest)
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_DB_PATH = "vector_db"

def retrieve_context(user_input: dict, k: int = 5) -> list[str]:
    db_path = Path(VECTOR_DB_PATH)
    if not (db_path / "index.faiss").exists():
        raise FileNotFoundError(
            f"FAISS index not found at {db_path}. Run `python ingest_docs.py` first."
        )

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = FAISS.load_local(
        str(db_path),
        embeddings,
        allow_dangerous_deserialization=True
    )

    query_text = user_input.get("request", "")
    results = vectorstore.similarity_search(query_text, k=k)
    return [r.page_content for r in results]