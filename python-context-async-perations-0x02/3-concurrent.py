import aiosqlite
import asyncio

# Asynchronous function to fetch all users
async def async_fetch_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("\nAll Users:")
            for user in users:
                print(user)

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            print("\nUsers Older than 40:")
            for user in older_users:
                print(user)

# Function to run both queries concurrently
async def fetch_concurrently():
    db_name = 'users.db'
    await asyncio.gather(
        async_fetch_users(db_name),
        async_fetch_older_users(db_name)
    )

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
