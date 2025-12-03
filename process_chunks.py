import pandas as pd

def explode_chunks(df_chunks: pd.DataFrame) -> pd.DataFrame:
    df = df_chunks.copy()
    df["point_id"] = range(len(df))
    return df
