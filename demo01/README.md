# Demo 01 — Toy Vectors and Cosine Similarity

## What is an Embedding?

An **embedding** is a way to represent a concept (a word, image, product, etc.) as a list of numbers — a **vector**. The idea is that similar concepts should end up with similar vectors, so we can do math on meaning.

In the real world, embeddings have hundreds or thousands of dimensions learned by a neural network. In this demo, we hand-craft 3-dimensional vectors so you can see the intuition clearly.

---

## The Three Dimensions Used Here

Each vector has exactly three slots:

```
[ animal-ness,  tech-ness,  food-ness ]
```

| Item   | Vector              | Interpretation                          |
|--------|---------------------|-----------------------------------------|
| cat    | `[0.90, 0.00, 0.10]` | Mostly animal, tiny bit food            |
| dog    | `[0.85, 0.00, 0.15]` | Mostly animal, tiny bit food            |
| python | `[0.30, 0.90, 0.00]` | Some animal, very techy (the language)  |
| pizza  | `[0.00, 0.05, 0.95]` | Almost pure food                        |

---

## What is Cosine Similarity?

Cosine similarity measures the **angle** between two vectors. It answers: *are these two vectors pointing in the same direction?*

```
cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)
```

- Returns **1.0** → identical direction (perfectly similar)
- Returns **0.0** → perpendicular (completely unrelated)
- Returns **-1.0** → opposite directions

> It ignores magnitude (length) and focuses only on direction — which is exactly what we want when comparing meaning.

---

## Step-by-Step: What the Code Does

### Step 1 — Define Toy Vectors

```python
cat    = np.array([0.9,  0.0,  0.1])
dog    = np.array([0.85, 0.0,  0.15])
python = np.array([0.3,  0.9,  0.0])
pizza  = np.array([0.0,  0.05, 0.95])
```

We manually assign values to each dimension based on what the word "means" in our tiny 3-feature space.

### Step 2 — Define the Similarity Function

```python
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

- `np.dot(a, b)` — dot product (numerator): how much the vectors agree
- `np.linalg.norm(...)` — magnitude (denominator): normalizes for vector length

### Step 3 — Compare All Pairs

```python
pairs = [
    ("cat",    "dog",    cat, dog),
    ("cat",    "python", cat, python),
    ("cat",    "pizza",  cat, pizza),
    ("python", "pizza",  python, pizza),
]
```

We loop over every pair and print the similarity score.

---

## Expected Output

```
Cosine Similarity Results:
----------------------------------------
  cat      ↔ dog       →  0.998   ← very similar (both animals)
  cat      ↔ python    →  0.286   ← different domains
  cat      ↔ pizza     →  0.110   ← almost unrelated
  python   ↔ pizza     →  0.050   ← completely unrelated
```

### Why does this make sense?

- **cat ↔ dog = 0.998** — both vectors are almost identical (`[high, 0, low]`) so they point in nearly the same direction.
- **cat ↔ python = 0.286** — cat is animal-heavy, python is tech-heavy; different directions.
- **cat ↔ pizza = 0.110** — animal vs food; almost nothing in common.
- **python ↔ pizza = 0.050** — tech vs food; practically orthogonal (unrelated).

---

## How to Run

> The virtual environment lives at `~/.venvs/item_embed` — a home-level folder shared across all demos in this project. No env inside the code tree.

### Step 1 — Create the shared virtual environment (one-time setup)

```bash
mkdir -p ~/.venvs
python3 -m venv ~/.venvs/item_embed
```

### Step 2 — Activate the virtual environment

**macOS / Linux:**
```bash
source ~/.venvs/item_embed/bin/activate
```

**Windows (Command Prompt):**
```bash
%USERPROFILE%\.venvs\item_embed\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
~\.venvs\item_embed\Scripts\Activate.ps1
```

Your terminal prompt will change to show `(item_embed)` — this confirms the environment is active.

### Step 3 — Install dependencies (one-time setup)

```bash
pip install numpy
```

### Step 4 — Run the script

```bash
cd /path/to/pksingh12/item_embed/demo01
python similarity_demo.py
```

### Step 5 — Deactivate when done

```bash
deactivate
```

> To run again later, only Steps 2 and 4 are needed — the environment and packages are already set up.

---

## Key Takeaway

> Cosine similarity lets you find "nearby" items in vector space.  
> Items that share the same kind of meaning land close together — items from different domains land far apart.

This is the foundation behind recommendation systems, semantic search, and item embeddings used in production ML systems.
