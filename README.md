# SemanticSQL-Cache: Intelligent Two-Tier Text-to-SQL Engine

An optimized, production-ready Text-to-SQL translation pipeline featuring a high-performance **Two-Tier Caching System**. This system translates complex natural language questions into safe, executable raw SQL queries against a relational SQLite database while minimizing expensive LLM and Embedding API overhead.
The "Red30-tech Classification & Clustering" dataset has been used for the system implementation. It can be downloaded from Kaggle.

---

## ⚡ Core Features & Capabilities

* **Natural Language to SQL:** Instantly converts human phrasing (e.g., *"rank states from the most to the least sales..."*) into syntactically valid SQL queries.
* **Two-Tier Cache Architecture:** Combines high-speed string matching with deep semantic vector understanding to maximize performance.
* **Persistent Disk Storage:** All cache tiers are written permanently to disk via SQLite, surviving script reloads, crashes, and server restarts.
* **Execution Guard (Anti-Poisoning):** Validates generated SQL against the database *before* committing it to the persistent cache, preventing broken queries from breaking future workflows.
* **Zero-Markdown Parsing:** Strips down LLM syntax artifacts, markdown code blocks, backticks, and double quotes for clean, direct execution.

---

## 🏗️ Architecture & Dual-Tier Caching Mechanics

To maximize speed and minimize resource utilization, the system filters incoming natural language queries through two distinct lookup layers before defaulting to local LLM inference:

<img width="1760" height="2416" alt="Image" src="https://github.com/user-attachments/assets/f147524c-a94a-4c37-8cb0-6d5143722fdd" />

1. **Tier 1: Exact Text Match (`query_cache`)**
   * **How it works:** Normalizes user text strings and executes an instantaneous local database lookup.
   * **Advantage:** Bypasses LLM and embedding API calls completely. Takes near-zero milliseconds.
2. **Tier 2: Semantic Match (`semantic_query_cache`)**
   * **How it works:** Calls local embeddings to convert user context into a vector space. It computes a mathematically bounded `cosine_similarity` check against previous intents.
   * **Advantage:** Handles syntax changes and rephrasing (e.g., *"show me sales by state"* will successfully map to *"rank states by total sales"* with a similarity score $\ge$ 0.88).

---

## 🛠️ Models & Stack Used

This architecture runs completely locally to maximize privacy and eliminate external licensing fees:

* **Inference Engine:** `ollama` (Local LLM Orchestration)
* **LLM Model:** `gemma3:4b` — Selected for advanced logical reasoning, strict adherence to system prompts, and structured code translation.
* **Embedding Model:** `nomic-embed-text-v2-moe` — A Mixture-of-Experts (MoE) text embedding model providing highly accurate vector representations for multi-phrase matching.
* **Database Layer:** `sqlite3` — Houses the primary enterprise tables (`retail_sales`) along with local cache schemas.
* **Data Processing:** `pandas` — Used for processing, structuring, and reading relational outputs into clean matrix dataframes.

---

## 🎯 Advantages over Standard Text-to-SQL

* **Cost & Token Efficiency:** Drastically reduces computational overhead and latency by serving recurring or similar queries out of local storage.
* **Robust Fail-Safe Routing:** If the LLM generates a broken query due to hallucination, the system intercepts the error, leaves the cache uncontaminated, and reports the exception cleanly.
* **Synonym Resilience:** Thanks to semantic vector thresholds, users don't need to memorize exact keywords to pull the correct historical metrics.

## System Test

<img width="818" height="576" alt="Image" src="https://github.com/user-attachments/assets/41e8e60a-a2ec-4d23-b760-001d3cce290f" />
<img width="717" height="298" alt="Image" src="https://github.com/user-attachments/assets/af9ef4be-db61-47b2-bc84-4024d75b0264" />
<img width="717" height="292" alt="Image" src="https://github.com/user-attachments/assets/6c699e6d-33dd-45d3-be89-3ffb7f96a798" />
<img width="741" height="291" alt="Image" src="https://github.com/user-attachments/assets/c25ed881-7d9f-45e2-b50f-7bb1c214c5be" />
