# 🧪 Research Index for Vector Store

This file lists all academic and practical sources used to populate the vector database for RAG-powered prompt completion. Each source should be summarized and chunked for ingestion.

---

## 📚 Papers + Sources

### 1. Schoenfeld, B. (2010)
**Title:** *The mechanisms of muscle hypertrophy and their application to resistance training*  
**Link:** https://pubmed.ncbi.nlm.nih.gov/20847704  
**Use:** Foundation for hypertrophy prompts, volume guidelines, rest periods

---

### 2. Helms, E., Morgan, G., et al. (2016)
**Title:** *Muscle and Strength Pyramid: Training*  
**Link:** https://muscleandstrengthpyramids.com  
**Use:** Periodization structure, MEV/MRV ranges, frequency templates

---

### 3. Zourdos, M., et al. (2016)
**Title:** *Daily Undulating Periodization and Strength Gains*  
**Link:** https://pubmed.ncbi.nlm.nih.gov/27182416  
**Use:** Advanced periodization logic for RAG recommendations

---

### 4. Nuckols, G. – Stronger by Science
**Title:** *Training Volume Benchmarks*  
**Link:** https://www.strongerbyscience.com  
**Use:** Muscle-specific volume targets by experience level

---

### 5. McDonald, L. – Bodyrecomposition.com
**Title:** *Deloading and recovery strategies*  
**Link:** https://bodyrecomposition.com  
**Use:** Recovery-based prompts and deload triggers

---

## 🧠 Plan for Vectorization

- Convert to `.txt` or `.md`
- Chunk into ~500 token sections
- Embed with `text-embedding-3-small` or SentenceTransformers
- Store in FAISS/Qdrant for RAG
