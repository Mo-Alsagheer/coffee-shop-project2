import sqlite3

# Create database connection
conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

# Create food menu table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS food_menu (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image_url TEXT
    )
"""
)

# Initial food menu data
foodMenu = [
    {
        "id": 1,
        "name": "Strawberry Tarts",
        "price": 10.99,
        "description": "Delicious strawberry tarts with a buttery crust and fresh strawberries on top.",
        "image_url": "static/images/Strawberry-Tarts.png",
    },
    {
        "id": 2,
        "name": "Cookies",
        "price": 5.99,
        "description": "Classic chocolate chip cookies, crispy on the outside and chewy on the inside.",
        "image_url": "static/images/Cookies.png",
    },
    {
        "id": 3,
        "name": "Hot Chocolate",
        "price": 12.99,
        "description": "Rich and creamy hot chocolate made with real cocoa and topped with whipped cream.",
        "image_url": "static/images/Cup-of-Hot-Chocolate.png",
    },
    {
        "id": 4,
        "name": "Strawberry & Blueberry Tarts",
        "price": 8.99,
        "description": "Creamy vanilla ice cream with a smooth texture and a rich flavor.",
        "image_url": "static/images/Strawberry-&-Blueberry-Tarts.png",
    },
    {
        "id": 5,
        "name": "Coffee & Pastries",
        "price": 15.99,
        "description": "Freshly brewed coffee served with a selection of assorted pastries.",
        "image_url": "static/images/Coffee-and-Pastries.png",
    },
]

# Convert dictionary data to tuple format for SQLite
food_data = [
    (food["id"], food["name"], food["price"], food["description"], food["image_url"])
    for food in foodMenu
]

# Insert data
# cursor.execute("DELETE FROM food_menu")  # Clear existing data
cursor.executemany("INSERT INTO food_menu VALUES (?, ?, ?, ?, ?)", food_data)

# Commit and close
conn.commit()
conn.close()

print("Database initialized successfully!")
