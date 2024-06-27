import mysql.connector
from datetime import date

date=date.today()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0252",
    database="MatchMyMantion"
)

class User_othintaction:
    def signup(self,user_name,email_id,password):
        global date

        cursor0 = conn.cursor()
        cursor0.execute("SELECT * FROM User_data WHERE user_name=%s ", (user_name,))
        user = cursor0.fetchone()
        if user:
            return False
        else:
            
            cursor = conn.cursor()
            cursor.execute("INSERT INTO User_data (user_name,user_email,user_password,user_joind) VALUES (%s,%s,%s,%s)", (user_name,email_id, password,date))
            conn.commit()
            return True

    def login(self,user_name,password):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_data WHERE user_name=%s AND user_password=%s", (user_name, password))
        user = cursor.fetchone()

        if user:
            # Login successful
            return True
        else:
            # Login failed
            return False
        
    def profile(self,user_name):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_data WHERE user_name=%s ", (user_name,))
        user = cursor.fetchone()
        if user:
            user_list = list(user)
            return user_list
        else:
            return None


