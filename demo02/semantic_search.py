# pip install sentence-transformers numpy
from sentence_transformers import SentenceTransformer
import numpy as np

# Step 1: Load a pre-trained embedding model
# all-MiniLM-L6-v2 outputs 384-dimensional vectors
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Define a tiny "knowledge base"
documents = [
    "How to reset your password in the admin panel",
    "Nutritional benefits of eating spinach daily",
    "Steps to configure Kubernetes pods for autoscaling",
    "Best hiking trails in the Western Ghats",
    "Understanding JWT tokens for API authentication",
]

# Step 3: Embed all documents (do this ONCE, store in a DB)
doc_embeddings = model.encode(documents, normalize_embeddings=True)
print(f"Each document → {doc_embeddings.shape[1]} dimensions")

# Step 4: Embed a query and find nearest documents
query = "I can't log into my account"
query_embedding = model.encode(query, normalize_embeddings=True)

# Step 5: Compute cosine similarity (dot product for normalized vectors)
similarities = np.dot(doc_embeddings, query_embedding)

# Step 6: Rank by similarity
ranked_indices = np.argsort(similarities)[::-1]  # descending

print(f"\nQuery: '{query}'\n")
print("Ranked results:")
for rank, idx in enumerate(ranked_indices, 1):
    print(f"  #{rank}  [{similarities[idx]:.3f}]  {documents[idx]}")

# EXPECTED OUTPUT:
#   #1  [0.562]  How to reset your password in the admin panel
#   #2  [0.318]  Understanding JWT tokens for API authentication
#   #3  [0.041]  Steps to configure Kubernetes pods for autoscaling
#   #4  [0.023]  Best hiking trails in the Western Ghats
#   #5  [0.008]  Nutritional benefits of eating spinach daily
#
# Notice: "reset your password" ranks #1 for "can't log in"
# even though they share ZERO keywords! That's semantic search.
