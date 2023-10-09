"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("birthDB.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    year,
    month,
    date_of_month,
    day_of_week,
    births,
):
    """create example query"""
    conn = sqlite3.connect("birthDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO birthDB
        (year, 
        month, 
        date_of_month, 
        day_of_week, 
        births) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            year,
            month,
            date_of_month,
            day_of_week,
            births,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO birthDB VALUES (
            {year}, 
            {month},
            {date_of_month}, 
            {day_of_week}, 
            {births});"""
    )


def update_record(
    year,
    month,
    date_of_month,
    day_of_week,
    births,
    record_id,
):
    """update example query"""
    conn = sqlite3.connect("birthDB.db")
    c = conn.cursor()
    print(
        (
            year,
            month,
            date_of_month,
            day_of_week,
            births,
            record_id,
        )
    )
    c.execute(
        """
        UPDATE birthDB 
        SET year=?,
        month=?, 
        date_of_month=?, 
        day_of_week=?, 
        births=?
        WHERE id=?;
        """,
        (
            year,
            month,
            date_of_month,
            day_of_week,
            births,
            record_id,
        ),
    )

    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE birthDB SET 
        year={year}, 
        month={month},
        date_of_month={date_of_month},
        day_of_week={day_of_week}, 
        births={births}
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("birthDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM birthDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM birthDB WHERE id={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("birthDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM birthDB")
    data = c.fetchall()
    log_query("SELECT * FROM birthDB;")
    return data
