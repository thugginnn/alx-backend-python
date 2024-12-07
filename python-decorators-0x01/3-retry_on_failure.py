import time
import sqlite3
import functools

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

def retry_on_failure(retries=3, delay=2):
    """Decorator to retry the function in case of failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(conn, *args, **kwargs)  # Try to execute the function
                except Exception as e:
                    attempts += 1
                    print(f"Error occurred: {e}. Retrying {attempts}/{retries}...")
                    if attempts < retries:
                        time.sleep(delay)  # Wait before retrying
                    else:
                        print("Max retries reached. Operation failed.")
                        raise  # After max retries, raise the exception
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Attempt to fetch users with automatic retry on failure
try:
    users = fetch_users_with_retry()
    print(users)
except Exception:
    print("Failed to fetch users after multiple attempts.")
