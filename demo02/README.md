# Demo 02 — Semantic Search with Real Embeddings

## What is Semantic Search?

Traditional keyword search matches **exact words**. Semantic search matches **meaning**.

A user typing `"I can't log into my account"` doesn't use the word "password" — but a semantic search engine still surfaces `"How to reset your password"` at rank #1 because the underlying *intent* is the same.

This is possible because a neural embedding model maps both phrases into nearby points in a high-dimensional vector space.

---

## How it Differs from Demo 01

| | Demo 01 | Demo 02 |
|---|---|---|
| Vectors | Hand-crafted (3 dimensions) | Neural network output (384 dimensions) |
| Dimensions | Manually assigned meaning | Learned from billions of text examples |
| Use case | Intuition building | Real-world semantic search |

---

## The Model: `all-MiniLM-L6-v2`

- A lightweight **sentence transformer** model (~80MB)
- Converts any sentence into a **384-dimensional vector**
- Trained to place semantically similar sentences close together in vector space
- `normalize_embeddings=True` makes each vector unit-length, so cosine similarity = dot product (faster)

---

## Step-by-Step: What the Code Does

### Step 1 — Load the model

```python
model = SentenceTransformer("all-MiniLM-L6-v2")
```

Downloads and loads the pre-trained model on first run (~80MB, cached locally after that).

### Step 2 — Define a knowledge base

```python
documents = [
    "How to reset your password in the admin panel",
    "Nutritional benefits of eating spinach daily",
    ...
]
```

In production this would be thousands of documents stored in a vector database.

### Step 3 — Embed all documents

```python
doc_embeddings = model.encode(documents, normalize_embeddings=True)
```

Each document becomes a 384-dimensional vector. Do this **once** and store the results — re-encoding on every query is wasteful.

### Step 4 — Embed the query

```python
query_embedding = model.encode(query, normalize_embeddings=True)
```

The user's query is embedded into the same 384-dimensional space.

### Step 5 — Compute similarity (dot product)

```python
similarities = np.dot(doc_embeddings, query_embedding)
```

Because both sides are normalized, the dot product equals cosine similarity. This gives one score per document.

### Step 6 — Rank and display

```python
ranked_indices = np.argsort(similarities)[::-1]  # descending order
```

`np.argsort` returns indices that would sort the array; `[::-1]` reverses to get highest-first.

---

## Expected Output

```
Each document → 384 dimensions

Query: 'I can't log into my account'

Ranked results:
  #1  [0.562]  How to reset your password in the admin panel
  #2  [0.318]  Understanding JWT tokens for API authentication
  #3  [0.041]  Steps to configure Kubernetes pods for autoscaling
  #4  [0.023]  Best hiking trails in the Western Ghats
  #5  [0.008]  Nutritional benefits of eating spinach daily
```

### Why this is remarkable

The query `"I can't log into my account"` shares **zero keywords** with `"How to reset your password"` — yet the model ranks it #1.

The model learned from massive text data that login failures and password resets are semantically linked. JWT authentication (#2) is also access-related, so it ranks above hiking trails and spinach.

---

## How to Run

> Uses the shared virtual environment at `~/.venvs/item_embed`.

### Step 1 — Activate the shared virtual environment (one-time setup if not done)

```bash
mkdir -p ~/.venvs
python3 -m venv ~/.venvs/item_embed
```

### Step 2 — Activate

**macOS / Linux:**
```bash
source ~/.venvs/item_embed/bin/activate
```

**Windows (Command Prompt):**
```bash
%USERPROFILE%\.venvs\item_embed\Scripts\activate.bat
```

Your prompt changes to `(item_embed)`.

### Step 3 — Install dependencies (one-time)

```bash
pip install sentence-transformers numpy
```

> `sentence-transformers` pulls in `torch` and `transformers` automatically. First install may take a few minutes.

### Step 4 — Run the script

```bash
cd demo02
python semantic_search.py
```

> First run downloads the model (~80MB) and caches it in `~/.cache/huggingface/`. Subsequent runs are instant.

### Step 5 — Deactivate when done

```bash
deactivate
```

---

## Key Takeaway

> Semantic search works because the model encodes **meaning**, not letters.  
> Two sentences with zero words in common can sit right next to each other in 384-dimensional space if they mean the same thing.

This is the foundation behind support ticket routing, FAQ matching, document retrieval, and recommendation engines.
