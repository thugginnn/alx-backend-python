import mysql.connector

def connect_to_database():
    """Connect to the users database."""
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

def stream_users_in_batches(batch_size):
    """Generator that fetches users in batches."""
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)  # Fetch rows as dictionaries
        cursor.execute("SELECT * FROM user_data")

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows

        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user['age'] > 25]
        for user in filtered_users:
            print(user)
