import aiosqlite
import asyncio

# Asynchronous function to fetch all users
async def async_fetch_users():
    print("Fetching all users...")
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("\nAll Users:")
            for user in users:
                print(user)

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
    print("Fetching users older than 40...")
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            print("\nUsers Older than 40:")
            for user in older_users:
                print(user)

# Function to run both queries concurrently using asyncio.gather
async def fetch_concurrently():
    print("Running fetch_concurrently...")
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
