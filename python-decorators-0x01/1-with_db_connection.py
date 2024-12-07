import sqlite3
import functools

def with_db_connection(func):
    """Decorator that opens a database connection and closes it after the function executes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open the database connection
        conn = sqlite3.connect('users.db')
        
        try:
            # Call the original function and pass the connection
            return func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed after the function executes
            conn.close()
    
    return wrapper

# Example function using the with_db_connection decorator
@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
