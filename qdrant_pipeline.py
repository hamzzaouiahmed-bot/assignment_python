import pickle
from qdrant_utils import insert_chunk, chunk_exists
from models_qdrant import ChunkMeta

def save_to_qdrant(df_chunks):
    for _, row in df_chunks.iterrows():
        point_id = row["point_id"]

        if chunk_exists(point_id):
            continue

        meta = ChunkMeta(
            article_title=row["article_title"],
            chunk_index=row["chunk_index"]
        )

        insert_chunk(point_id, row["embedding"], meta)
