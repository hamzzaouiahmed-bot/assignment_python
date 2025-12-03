import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from chunking import chunk_text
<<<<<<< HEAD
import pickle
=======
>>>>>>> 89779f1c9768fe7252f0cdd634bb9f545b154801

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

<<<<<<< HEAD
df = pd.read_csv("articles.csv", dtype=str)

all_rows = []

for _, row in df.iterrows():
    chunks = chunk_text(row["summary"])

    for i, ch in enumerate(chunks):
        emb = genai.embed_content(
            model="models/text-embedding-004",
            content=ch
        )

        all_rows.append({
            "article_title": row["title"],
            "chunk_index": i,
            "chunk_text": ch,
            "embedding": emb["embedding"]
        })

df_chunks = pd.DataFrame(all_rows)

pickle.dump(df_chunks, open("embeddings.pkl", "wb"))

print("Done. Number of chunks:", len(df_chunks))
=======
df = pd.read_csv("articles.csv", dtype="string")

if "text" in df.columns:
    col = "text"
else:
    col = "summary"

df["chunks"] = df[col].astype("string").apply(
    lambda t: chunk_text(t, chunk_size=120, overlap=30)
)

rows = []

for _, row in df.iterrows():
    title = row["title"]
    for i, chunk in enumerate(row["chunks"]):
        rows.append({
            "article_title": title,
            "chunk_index": i,
            "chunk_text": chunk
        })

df_chunks = pd.DataFrame(rows, dtype="string")

embeddings = []

for chunk in df_chunks["chunk_text"]:
    r = genai.embed_content(
        model="models/text-embedding-004",
        content=str(chunk)
    )
    embeddings.append(r["embedding"])

df_chunks["embedding"] = embeddings

df_chunks.to_pickle("embeddings.pkl")

print("Done. Number of chunks:", len(df_chunks))
print("Embeddings saved to embeddings.pkl")
>>>>>>> 89779f1c9768fe7252f0cdd634bb9f545b154801
