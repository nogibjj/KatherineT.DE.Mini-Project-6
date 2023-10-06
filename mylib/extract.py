"""
Extract a dataset from a URL. 
JSON or CSV formats tend to work well
"""
import os
import requests


def extract(
    url="""https://github.com/fivethirtyeight/data/blob/master/births/US_births_2000-2014_SSA.csv""",
    file_path="data/births/US_births_2000-2014_SSA.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
