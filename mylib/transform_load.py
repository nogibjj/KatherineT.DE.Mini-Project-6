"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv

def load(dataset="data/fifa.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Load CSV data into a list of tuples
    with open(dataset, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # skip header
        data_list = [tuple(row) for row in reader]
    
    # Debugging: Print the first few rows to inspect data
    for row in data_list[:5]:
        print(row)
        if len(row) != 5:
            print(f"Row does not have 5 columns: {row}")

    conn = sqlite3.connect('fifaDB.db')
    c = conn.cursor()

    # (Re)Create the table
    c.execute("DROP TABLE IF EXISTS fifaDB")
    c.execute("""
              CREATE TABLE fifaDB (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    country TEXT, 
                    confederation TEXT,
                    population_share REAL,
                    tv_audience_share REAL,
                    gdp_weighted_share REAL
                  )
              """)
    
    # Insert data
    try:
        c.executemany("""
                      INSERT INTO fifaDB (
                            country, 
                            confederation,
                            population_share ,
                            tv_audience_share ,
                            gdp_weighted_share
                          ) 
                          VALUES (?, ?, ?, ?, ?)
                      """, data_list)
    except Exception as e:
        print(f"Error while inserting data: {e}")
        conn.rollback()
    else:
        conn.commit()
    finally:
        conn.close()

    return "fifaDB.db"
