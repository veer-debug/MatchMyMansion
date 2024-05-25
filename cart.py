from datetime import date
import mysql.connector

date=date.today()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MatchMyMantion"
)
class Cart :
    def add_to_cart(user_name,product_id):

        cursor = conn.cursor()
        cursor.execute("INSERT INTO User_cart (user_name,product_id) VALUES (%s,%s)", (user_name,product_id))
        conn.commit()
        return True
    
    def user_cart_data(user_name):
        cursor=conn.cursor()
        cursor.execute("select*from User_cart where user_name=%s",(user_name,))
        user = cursor.fetchone()
        if user:
            row_list = [list(row) for row in user]
            return row_list
        else:
            return None


       

