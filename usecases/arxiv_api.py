from __future__ import annotations

import pandas as pd
import requests
import xml.etree.ElementTree as ET


URL = "http://export.arxiv.org/api/query"


def fetch_arxiv_xml(query: str, max_results: int = 10) -> str:
    r = requests.get(
        URL,
        params={"search_query": f"all:{query}", "start": 0, "max_results": max_results},
        timeout=30,
    )
    r.raise_for_status()
    return r.text


def parse_arxiv_xml_to_dataframe(xml: str) -> pd.DataFrame:
    root = ET.fromstring(xml)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    rows = []

    for e in root.findall("atom:entry", ns):
        title = e.find("atom:title", ns).text or ""
        summary = e.find("atom:summary", ns).text or ""
        arxiv_id = e.find("atom:id", ns).text.rsplit("/", 1)[-1]

        author_el = e.find("atom:author", ns)
        author_full_name = ""
        if author_el is not None:
            nm = author_el.find("atom:name", ns)
            author_full_name = nm.text if nm is not None else ""

        rows.append(
            {
                "title": title,
                "summary": summary,
                "file_path": "",
                "arxiv_id": arxiv_id,
                "author_full_name": author_full_name,
                "author_title": "",
            }
        )

    return pd.DataFrame(rows, dtype="string")
