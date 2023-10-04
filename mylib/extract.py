"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well

world cup dataset
"""
import requests
import os

def extract(
    url="""
    https://projects.fivethirtyeight.com/soccer-api/international/2022/wc_matches.csv
    """,
    file_path="data/wc_matches.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path






