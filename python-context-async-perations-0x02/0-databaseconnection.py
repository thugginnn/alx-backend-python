import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        # Open the connection and return the cursor
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection automatically when exiting the context
        self.connection.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")

# Usage of the context manager
if __name__ == "__main__":
    # Assume the database 'users.db' exists with a 'users' table
    with DatabaseConnection('users.db') as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        
        # Print the results from the query
        for row in results:
            print(row)
