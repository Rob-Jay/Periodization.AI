# Periodization.AI

Your intelligent, performance-focused training assistant powered by Retrieval-Augmented Generation (RAG).

## 🚀 Overview
Periodization.AI helps athletes and serious lifters:
- Generate structured, evidence-based training cycles
- Track progress across mesocycles
- Adapt to fatigue, missed sessions, and under/overtraining
- Communicate with the assistant using natural language (or voice)

> **Goal:** Build the most insightful, personalized training assistant possible — grounded in training science, not aesthetics.

---

## 📦 Project Structure
```
Periodization.AI/
├── README.md                  # Project overview
├── .gitignore                 # Git ignore rules for Python + Node
├── LICENSE                    # MIT (you can change later)
├── mobile-app/                # React Native frontend
├── backend-api/               # FastAPI or Spring Boot API
├── rag-engine/                # LangChain, prompt templates, LLM scripts
│   ├── prompts/
│   │   └── strength_mesocycle_prompt.json
│   └── ingest_docs.py
├── diagrams/                  # Architecture + UML diagrams
│   ├── architecture.puml
│   └── architecture.png
├── docs/                      # Notes, science summaries, dev logs
│   └── periodization_principles.md
├── db/                        # SQL schemas or Supabase exports
└── tests/                     # Unit + integration tests
```

---

## 🔧 Tech Stack

### MVP Focus
- **Frontend:** React Native (Expo)
- **Backend:** FastAPI (Python preferred for LangChain)
- **LLM Integration:** OpenAI (initial), Mistral/local (later)
- **Vector Store:** FAISS or Qdrant
- **DB:** Supabase (Postgres)
- **Diagramming:** PlantUML for architecture

---

## 🌱 Getting Started
1. Clone the repo:
```bash
git clone https://github.com/yourname/Periodization.AI.git
cd Periodization.AI
```

2. Create virtual environments and install dependencies in respective folders

3. Start development in:
   - `mobile-app/` → frontend
   - `backend-api/` → backend API
   - `rag-engine/` → model + prompt logic

4. Keep notes in `docs/` and update diagrams in `diagrams/`

---

## 📋 License
MIT License — free for personal and academic use. You can update this if you want to keep it proprietary.

---

## 🙌 Contributions
This is a solo project for now, but future contributions may be welcome. Please submit issues or ideas if you want to collaborate.
