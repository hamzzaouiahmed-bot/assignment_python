<<<<<<< HEAD
def chunk_text(text: str, chunk_size: int = 80, overlap: int = 20):
    words = text.split()
    chunks = []
    start = 0
    
=======
def chunk_text(text: str, chunk_size: int = 100, overlap: int = 20) -> list[str]:
    words = text.split()
    chunks = []
    start = 0

>>>>>>> 89779f1c9768fe7252f0cdd634bb9f545b154801
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
<<<<<<< HEAD
        start += chunk_size - overlap
    
=======
        start += (chunk_size - overlap)

>>>>>>> 89779f1c9768fe7252f0cdd634bb9f545b154801
    return chunks
