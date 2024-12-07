import sqlite3
import functools
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_queries(func):
    """Decorator to log SQL queries before executing the function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query', '')  # Get the query from the keyword arguments
        logging.info(f"Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper

# Example function using the log_queries decorator
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
