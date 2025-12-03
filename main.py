<<<<<<< HEAD
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
=======
<<<<<<< HEAD
from __future__ import annotations

import logging

from storage.sql import get_session
from storage.mongo import init_mongo
from models.sql_models import Base
from storage.sql import engine

from usecases.arxiv_api import fetch_arxiv_xml, parse_arxiv_xml_to_dataframe
from usecases.html_content import add_html_column
from usecases.mariadb_loader import load_dataframe_to_mariadb
from usecases.mongodb_loader import load_dataframe_to_mongodb
from usecases.search_mongo import search_scientific_articles

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main() -> None:
    log.info("Initializing MariaDB")
    Base.metadata.create_all(bind=engine)

    log.info("Initializing MongoDB")
    init_mongo()

    log.info("Fetching ArXiv data")
    xml = fetch_arxiv_xml("machine learning", max_results=5)

    log.info("Parsing XML")
    df = parse_arxiv_xml_to_dataframe(xml)

    log.info("Fetching HTML pages")
    df_html = add_html_column(df)

    log.info("Saving into MariaDB")
    df_maria = load_dataframe_to_mariadb(df_html)

    log.info("Saving into MongoDB")
    df_mongo = load_dataframe_to_mongodb(df_maria)

    log.info("Testing search")
    results = search_scientific_articles("learning")
    for r in results:
        print(r.title)
=======
<<<<<<< HEAD
from __future__ import annotations

from storage.mariadb import init_db
from storage.mongodb import init_mongodb
from usecases.load_csv_to_mariadb import load_csv_to_mariadb
from usecases.mariadb_to_mongodb import transfer_mariadb_to_mongodb
from usecases.search_mongodb import search_mongodb


def main() -> None:

    init_db()


    init_mongodb(host="localhost", port=27018, db_name="assignment07")


    print("Loading CSV into MariaDB...")
    load_csv_to_mariadb()
    print("Done.")


    print("Transferring data from MariaDB to MongoDB...")
    transfer_mariadb_to_mongodb()
    print("Done.")

 
    print("Searching in MongoDB for 'quantum")
    results = search_mongodb("quantum")
    for doc in results:
        print(f"- {doc.title} ({doc.arxiv_id})")
>>>>>>> 4dfded0873f17fd67aeb3e3c124e54d1cd93d79f


if __name__ == "__main__":
    main()
<<<<<<< HEAD
=======
=======
from typing import TypedDict
from collections import namedtuple
from dataclasses import dataclass
from pydantic import BaseModel
import numpy as np
import pandas as pd
import time


class UserTD(TypedDict):
    id: int
    name: str
    age: int
    email: str

UserNT = namedtuple("UserNT", ["id", "name", "age", "email"])

@dataclass
class UserDC:
    id: int
    name: str
    age: int
    email: str

class UserPD(BaseModel):
    id: int
    name: str
    age: int
    email: str


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def multiply_list(lst, scalar):
    return [x * scalar for x in lst]

@timer
def multiply_numpy(arr, scalar):
    return arr * scalar


num_array = np.array([1, 2, 3, 4, 5])
num_list = [1, 2, 3, 4, 5]


multiply_list(num_list, 10)
multiply_numpy(num_array, 10)



df = pd.read_csv("users.csv")
print(df)


big_list = list(range(1_000_000))
big_array = np.array(big_list)

multiply_list(big_list, 10)
multiply_numpy(big_array, 10)
>>>>>>> 8393d2e6d30899ff74a4e8029bc744f944846dc6
>>>>>>> 4dfded0873f17fd67aeb3e3c124e54d1cd93d79f
>>>>>>> 89779f1c9768fe7252f0cdd634bb9f545b154801
