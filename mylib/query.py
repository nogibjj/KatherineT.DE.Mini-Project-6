"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def create_record(
    country, confederation, population_share, tv_audience_share, gdp_weighted_share
):
    """create example query"""
    conn = sqlite3.connect("fifaDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO fifaDB 
        (country, 
        confederation, 
        population_share,
        tv_audience_share, 
        gdp_weighted_share) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (country, 
         confederation, 
         population_share, 
         tv_audience_share, 
         gdp_weighted_share),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""INSERT INTO fifaDB VALUES (
                {country}, 
                {confederation},
                {population_share},
                {tv_audience_share},
                {gdp_weighted_share});"""
    )


def read_data():
    """read data"""
    conn = sqlite3.connect("fifaDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM fifaDB")
    data = c.fetchall()
    log_query("SELECT * FROM fifaDB;")
    return data


def update_record(
            record_id,
            country, 
            confederation, 
            population_share, 
            tv_audience_share, 
            gdp_weighted_share
):
    """update example query"""
    conn = sqlite3.connect("fifaDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE fifaDB 
        SET country=?, 
        confederation=?, 
        population_share=?, 
        tv_audience_share=?, 
        gdp_weighted_share=?
        WHERE id=?
        """,
        (
            country, 
            confederation, 
            population_share, 
            tv_audience_share, 
            gdp_weighted_share,
            record_id
        ),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""UPDATE fifaDB SET 
        country={country}, 
        confederation=
        {confederation},
        population_share={population_share}, 
        tv_audience_share={tv_audience_share}, 
        gdp_weighted_share={gdp_weighted_share},
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("fifaDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM fifaDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    log_query(f"DELETE FROM fifaDB WHERE id={record_id};")
