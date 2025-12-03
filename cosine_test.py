import os
from dotenv import load_dotenv
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

phrases = [
    "The cat is sleeping",
    "A dog is running",
    "Quantum physics studies matter and energy"
]

embs = []

for p in phrases:
    r = genai.embed_content(
        model="models/text-embedding-004",
        content=p
    )
    embs.append(r["embedding"])

print("Cosine similarity:")
print(cosine_similarity(embs))
