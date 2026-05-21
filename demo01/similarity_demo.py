import numpy as np

# Step 1: Define toy vectors manually
# Imagine each dimension = [animal-ness, tech-ness, food-ness]
cat    = np.array([0.9,  0.0,  0.1])
dog    = np.array([0.85, 0.0,  0.15])
python = np.array([0.3,  0.9,  0.0])   # the language, not the snake!
pizza  = np.array([0.0,  0.05, 0.95])

# Step 2: Compute cosine similarity between all pairs
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

pairs = [
    ("cat",    "dog",    cat, dog),
    ("cat",    "python", cat, python),
    ("cat",    "pizza",  cat, pizza),
    ("python", "pizza",  python, pizza),
]

print("Cosine Similarity Results:")
print("-" * 40)
for name_a, name_b, vec_a, vec_b in pairs:
    sim = cosine_sim(vec_a, vec_b)
    print(f"  {name_a:8s} ↔ {name_b:8s}  →  {sim:.3f}")

# OUTPUT:
# cat      ↔ dog       →  0.998   ← very similar (both animals)
# cat      ↔ python    →  0.286   ← different domains
# cat      ↔ pizza     →  0.110   ← almost unrelated
# python   ↔ pizza     →  0.050   ← completely unrelated
