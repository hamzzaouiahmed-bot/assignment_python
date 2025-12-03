from pydantic import BaseModel

class ChunkMeta(BaseModel):
    article_title: str
    chunk_index: int
