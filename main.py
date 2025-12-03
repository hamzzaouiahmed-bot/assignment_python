from qdrant_init import init_qdrant_collection
from qdrant_pipeline import save_to_qdrant
from semantic_search import search
from process_chunks import explode_chunks
import pickle

def main():

    print("Creating Qdrant collection")
    init_qdrant_collection()

    print("Loading embeddings")
    df_chunks = pickle.load(open("embeddings.pkl", "rb"))

    print("Exploding chunks")
    df = explode_chunks(df_chunks)

    print("Saving to Qdrant")
    save_to_qdrant(df)

    print("Testing semantic search")
    results = search("neural networks")

    for r in results:
        print(r.payload)

if __name__ == "__main__":
    main()
