from datetime import date
import mysql.connector

today_date = date.today()

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9954"
)

cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS MatchMyMantion")
cursor.execute("USE MatchMyMantion")

# Create the 'User_data' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS User_data (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        user_email VARCHAR(255),
        user_password VARCHAR(255)
    )
""")

# Create the 'User_wishlist' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS User_wishlist (
        wishlist_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        product_id INT,
        FOREIGN KEY (user_id) REFERENCES User_data(user_id)
    )
""")

# Close the initial connection after creating the database and tables
cursor.close()

# Reconnect to the 'MatchMyMantion' database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9954",
    database="MatchMyMantion"
)

class Cart:
    @staticmethod
    def add_to_cart(username, product_id):
        cursor = conn.cursor()
        
        # Get user_id for the given username
        cursor.execute("SELECT user_id FROM User_data WHERE user_name = %s", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]

            # Insert wishlist items
            cursor.execute("INSERT INTO User_wishlist (user_id, product_id) VALUES (%s, %s)", (user_id, product_id))

            # Commit the wishlist insert
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    @staticmethod
    def user_cart(user_name):
        p_id = []
        cursor = conn.cursor()

        # Query to fetch wishlist for the given username
        cursor.execute("""SELECT u.user_name, w.product_id 
                          FROM User_data u JOIN User_wishlist w 
                          ON u.user_id = w.user_id WHERE u.user_name = %s """, (user_name,))

        # Fetch and print the results
        wishlist_items = cursor.fetchall()
        for item in wishlist_items:
            p_id.append(item[1])
        cursor.close()
        return p_id
