import os

import google.generativeai as genai
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

client = QdrantClient(host="localhost", port=6333)


def search(query: str, top_k: int = 5):
    q_embed = genai.embed_content(
        model="models/text-embedding-004",
        content=query,
    )["embedding"]

    results = client.search(
        collection_name="article_chunks",
        query_vector=q_embed,
        limit=top_k,
        with_payload=True,
    )

    return results
