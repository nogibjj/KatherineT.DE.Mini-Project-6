"""
Transforms and Loads data into Azure Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/births2000.csv", dataset2="data/births1994.csv"):
    """Transforms and Loads data into the local databricks database"""
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        # INSERT TAKES TOO LONG
        # c.execute("DROP TABLE IF EXISTS births2000")
        c.execute("SHOW TABLES FROM default LIKE 'year*'")
        result = c.fetchall()
        # takes too long so not dropping anymore
        # c.execute("DROP TABLE IF EXISTS births1994")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS births2000 (
                    id int,
                    year int,
                    month int,
                    date_of_month int,
                    day_of_week int,
                    births int
                )
            """
            )
            # insert
            for _, row in df.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO births2000DB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'year*'")
        result = c.fetchall()
        # c.execute("DROP TABLE IF EXISTS births1994DB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS births1994DB (
                    id int,
                    year int,
                    month int,
                    date_of_month int,
                    day_of_week int,
                    births
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO births1994DB VALUES {convert}")
        c.close()

    return "success"
