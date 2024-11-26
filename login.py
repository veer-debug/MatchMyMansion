import mysql.connector
from datetime import date

# Get today's date
date = date.today()

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
        user_password VARCHAR(255),
        user_joind DATE NOT NULL
    )
""")

# Close the cursor
cursor.close()

# Reconnect to the 'MatchMyMantion' database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9954",
    database="MatchMyMantion"
)

class User_othintaction:
    def signup(self, user_name, email_id, password):
        global date

        cursor0 = conn.cursor()
        cursor0.execute("SELECT * FROM User_data WHERE user_name=%s ", (user_name,))
        user = cursor0.fetchone()
        if user:
            return False
        else:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO User_data (user_name, user_email, user_password, user_joind) VALUES (%s, %s, %s, %s)", (user_name, email_id, password, date))
            conn.commit()
            cursor.close()
            return True

    def login(self, user_name, password):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_data WHERE user_name=%s AND user_password=%s", (user_name, password))
        user = cursor.fetchone()

        if user:
            # Login successful
            cursor.close()
            return True
        else:
            # Login failed
            cursor.close()
            return False
        
    def profile(self, user_name):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_data WHERE user_name=%s ", (user_name,))
        user = cursor.fetchone()
        if user:
            user_list = list(user)
            cursor.close()
            return user_list
        else:
            cursor.close()
            return None
