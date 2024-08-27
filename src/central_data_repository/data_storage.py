# data_storage.py
"""
Handles storing and retrieving data in the Central Data Repository.
"""

import sqlite3
from common.logging import setup_logging

logger = setup_logging()

def store_data(data, table_name):
    """
    Stores data in a specified table within the database.
    Args:
        data: Data to be stored.
        table_name: Name of the table where data will be stored.
    """
    conn = sqlite3.connect('central_data_repository.db')
    data.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    logger.info(f"Data stored in table {table_name}")

def retrieve_data(query):
    """
    Retrieves data from the database based on a SQL query.
    Args:
        query: SQL query to execute.
    Returns:
        Retrieved data.
    """
    conn = sqlite3.connect('central_data_repository.db')
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

if __name__ == "__main__":
    # Example usage
    data = retrieve_data("SELECT * FROM anomalies")
    logger.info(f"Data retrieved: {data.head()}")
