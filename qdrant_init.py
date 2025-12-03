from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(host="localhost", port=6333)

def init_qdrant_collection():
    client.recreate_collection(
        collection_name="article_chunks",
        vectors_config=models.VectorParams(
            size=768,
            distance=models.Distance.COSINE
        )
    )
