"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well
"""
import os
import requests
import pandas as pd


def extract(
    url="""
    https://github.com/fivethirtyeight/data/blob/master/births/US_births_2000-2014_SSA.csv?raw=true
    """,
    url2="""
    https://github.com/fivethirtyeight/data/blob/master/births/US_births_1994-2003_CDC_NCHS.csv?raw=true
    """,
    file_path="data/births2000.csv",
    file_path2="data/births1994.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, "wb") as f:
            f.write(r.content)
    df1 = pd.read_csv(file_path)
    df2 = pd.read_csv(file_path2)
    df_subset1 = df1.head(150)
    df_subset2 = df2.head(150)

    df_subset1.to_csv(file_path, index=False)
    df_subset2.to_csv(file_path2, index=False)
    return file_path, file_path2