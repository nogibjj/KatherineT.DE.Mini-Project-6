"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv

def load(dataset="data/births/US_births_2000-2014_SSA.csv"):
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

    conn = sqlite3.connect('USBirthDB.db')
    c = conn.cursor()

    # (Re)Create the table
    c.execute("DROP TABLE IF EXISTS USBirthDB")
    c.execute("""
              CREATE TABLE USBirthDB (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    year INT, 
                    month INT,
                    date_of_month INT,
                    day_of_week INT,
                    births INT
                  )
              """)
    
    # Insert data
    try:
        c.executemany("""
                      INSERT INTO USBirthDB (
                            year, 
                            month,
                            date_of_month ,
                            day_of_week ,
                            births
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

    return "USBirthDB.db"








































