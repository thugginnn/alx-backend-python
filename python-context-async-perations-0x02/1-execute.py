import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params else []

    def __enter__(self):
        # Open the connection and create a cursor
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self._execute_query()

    def _execute_query(self):
        # Execute the query with the provided parameters
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection automatically
        self.connection.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")

# Usage of the context manager
if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery('users.db', query, params) as results:
        for row in results:
            print(row)
