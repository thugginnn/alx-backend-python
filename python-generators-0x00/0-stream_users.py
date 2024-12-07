import mysql.connector

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='prodev_user',
            password='Secure@7890',
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def stream_users():
    """Generator that streams rows from the user_data table one by one."""
    connection = connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)  # Fetch rows as dictionaries
        cursor.execute("SELECT * FROM user_data")
        
        for row in cursor:
            yield row

        cursor.close()
        connection.close()
