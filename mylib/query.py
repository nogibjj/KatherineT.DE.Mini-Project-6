"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def create_record(
    year, month, date_of_month, day_of_week, births
):
    """create example query"""
    conn = sqlite3.connect("USBirthDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO USBirthDB 
        (year, 
        month, 
        date_of_month,
        day_of_week, 
        births) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (year, 
         month, 
         date_of_month, 
         day_of_week, 
         births),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""INSERT INTO fifaDB VALUES (
                {year}, 
                {month},
                {date_of_month},
                {day_of_week},
                {births});"""
    )


def read_data():
    """read data"""
    conn = sqlite3.connect("USBirthDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM USBirthDB")
    data = c.fetchall()
    log_query("SELECT * FROM USBirthDB;")
    return data


def update_record(
            record_id,
            year, 
            month, 
            date_of_month, 
            day_of_week, 
            births
):
    """update example query"""
    conn = sqlite3.connect("USBirthDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE USBirthDB 
        SET year=?, 
        month=?, 
        date_of_month=?, 
        day_of_week=?, 
        births=?
        WHERE id=?
        """,
        (
            year, 
            month, 
            date_of_month, 
            day_of_week, 
            births,
            record_id
        ),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""UPDATE USBirthDB SET 
        year={year}, 
        month=
        {month},
        date_of_month={date_of_month}, 
        day_of_week={day_of_week}, 
        births={births},
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("USBirthDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM USBirthDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    log_query(f"DELETE FROM USBirthDB WHERE id={record_id};")