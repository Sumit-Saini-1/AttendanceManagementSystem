from db import db
cursor=db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50),email VARCHAR(50),password VARCHAR(20))")

class User:
    @staticmethod
    def create_user(username, email, password):
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (username, email, password)
        try:
            with db.cursor() as cursor:
                cursor.execute(query, values)
                db.commit()
        except Exception as e:
            print("Error creating user:", e)

    @staticmethod
    def get_user(email):
        query = "SELECT * FROM users WHERE email = %s"
        values = (email,)
        try:
            with db.cursor() as cursor:
                cursor.execute(query, values)
                data = cursor.fetchone()
                return data
        except Exception as e:
            print("Error getting user:", e)
            return None