# rag_engine/ingest_docs.py  (HuggingFace embeddings version – no API key needed)
from pathlib import Path
import glob
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Config
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
VECTOR_DB_PATH = "vector_db"

def load_docs(directory: str) -> list[str]:
    docs = []
    for filepath in glob.glob(str(Path(directory) / "*.txt")):
        with open(filepath, "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs

def chunk_and_embed(docs: list[str]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    chunks = []
    for doc in docs:
        chunks.extend(splitter.split_text(doc))

    # 🧠 Local, free embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vs = FAISS.from_texts(chunks, embedding=embeddings)

    out_dir = Path(VECTOR_DB_PATH)
    out_dir.mkdir(parents=True, exist_ok=True)
    vs.save_local(str(out_dir))
    print(f"✅ Saved FAISS index to: {out_dir.resolve()}")

if __name__ == "__main__":
    src = Path(__file__).parent.parent / "docs_source"
    docs = load_docs(str(src))
    if not docs:
        raise SystemExit(f"❌ No .txt files found in {src}. Add sources then re-run.")
    chunk_and_embed(docs)