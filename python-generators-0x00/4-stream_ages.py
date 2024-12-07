import mysql.connector
from seed import connect_to_prodev

def stream_user_ages():
    """A generator that yields user ages one by one from the database."""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    connection.close()

def calculate_average_age():
    """Calculates the average age of users using the stream_user_ages generator."""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count == 0:
        return 0  # To prevent division by zero if there are no users
    return total_age / count

# Main script to output the average age
average_age = calculate_average_age()
print(f"Average age of users: {average_age:.2f}")
