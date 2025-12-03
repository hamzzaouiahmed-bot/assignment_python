import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from chunking import chunk_text
import pickle

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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
