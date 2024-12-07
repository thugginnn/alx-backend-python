import time
import sqlite3
import functools

# This dictionary will hold cached query results
query_cache = {}

def with_db_connection(func):
    """Decorator to handle opening and closing the database connection."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    """Decorator to cache the query results."""
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if the result of this query is already cached
        if query in query_cache:
            print("Fetching result from cache...")
            return query_cache[query]  # Return the cached result
        
        # Otherwise, call the original function to execute the query
        result = func(conn, query, *args, **kwargs)
        
        # Cache the result of the query
        print("Caching the result...")
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will execute the query and cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
