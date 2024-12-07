import mysql.connector
from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """Fetch a specific page of users with the given page size and offset."""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """Generator function to lazily fetch pages of users."""
    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            break
        yield users
        offset += page_size
