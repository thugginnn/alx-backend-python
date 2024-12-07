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

def transactional(func):
    """Decorator to manage database transactions (commit/rollback)."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Start a transaction
            result = func(conn, *args, **kwargs)
            # Commit the transaction if the function executes successfully
            conn.commit()
            return result
        except Exception as e:
            # Rollback the transaction if an error occurs
            conn.rollback()
            print(f"Error occurred: {e}")
            raise  # Re-raise the exception after rollback
    return wrapper

# Example function using both the with_db_connection and transactional decorators
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Update user's email with automatic transaction handling
try:
    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
    print("Email updated successfully.")
except Exception:
    print("Failed to update email.")
