from qdrant_client import QdrantClient
from qdrant_client.http import models
from models_qdrant import ChunkMeta

client = QdrantClient(host="localhost", port=6333)

def insert_chunk(point_id: int, vector: list[float], meta: ChunkMeta) -> None:
    client.upsert(
        collection_name="article_chunks",
        points=[
            models.PointStruct(
                id=point_id,
                vector=vector,
                payload=meta.model_dump()
            )
        ]
    )

def chunk_exists(point_id: int) -> bool:
    res = client.retrieve(
        collection_name="article_chunks",
        ids=[point_id]
    )
    return len(res) > 0
