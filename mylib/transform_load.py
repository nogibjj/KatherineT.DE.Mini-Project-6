"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv

def load(dataset="data/wc_forecasts.csv"):
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

    conn = sqlite3.connect('wc_forecastsDB.db')
    c = conn.cursor()

    # (Re)Create the table
    c.execute("DROP TABLE IF EXISTS wc_forecastsDB")
    c.execute("""
              CREATE TABLE wc_forecastsDB (
              team TEXT,
              group TEXT,
              spi REAL,
              global_o REAL,
              global_d REAL,
              sim_wins REAL
                  )
              """)
    
    # Insert data
    try:
        c.executemany("""
                      INSERT INTO wc_forecastsDB (
              group,
              spi,
              global_o,
              global_d,
              sim_wins
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

    return "wc_forecastsDB.db"
