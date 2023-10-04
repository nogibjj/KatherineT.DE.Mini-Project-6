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
    conn = sqlite3.connect("wc_forecastsDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO fifaDB 
        (group, 
        spi, 
        global_o,
        global_d, 
        sim_wins) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (group, 
         spi, 
         offensive_rating, 
         defensive_rating, 
         sim_wins),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""INSERT INTO fifaDB VALUES (
                {group}, 
                {spi},
                {offensive_rating},
                {defensive_rating},
                {sim_wins});"""
    )


def read_data():
    """read data"""
    conn = sqlite3.connect("wc_forecastsDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM wc_forecastsDB")
    data = c.fetchall()
    log_query("SELECT * FROM wc_forecastsDB;")
    return data


def update_record(
            team,
            group, 
            spi, 
            offensive_rating, 
            defensive_rating, 
            sim_wins
):
    """update example query"""
    conn = sqlite3.connect("wc_forecastsDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE fifaDB 
        SET group=?, 
        spi=?, 
        offensive_rating=?, 
        defensive_rating=?, 
        sim_wins=?
        WHERE team=?
        """,
        (
            group, 
            spi, 
            offensive_rating, 
            defensive_rating, 
            sim_wins,
            team
        ),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""UPDATE fifaDB SET 
        group={group}, 
        spi={spi},
        offensive_rating={offensive_rating}, 
        defensive_rating={defensive_rating}, 
        sim_wins={sim_wins},
        WHERE team={team};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("wc_forecastsDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM wc_forecastsDB WHERE team=?", (team,))
    conn.commit()
    conn.close()

    log_query(f"DELETE FROM wc_forecastsDB WHERE team={team};")
