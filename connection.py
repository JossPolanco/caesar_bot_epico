import psycopg
from PswEncryption import PswEncription

conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="jpolanco4515#",
    port="5432"
)

pwsEncription = PswEncription()

def createUser(username, password):
    try:
        query = "INSERT INTO TBL_USERS (username, password) VALUES (%s, %s)"
        
        passwordHashed = pwsEncription.hashPassword(password)
        values = (username, passwordHashed)
        
        conn.execute(query, values)
        conn.commit()
        
        return {
            "status": "ok",
            "response": "User successfully created"
        }
        
    except Exception as error:
        conn.rollback()
        print(error)
        return {
            "status": "error",
            "response": "An error has occurred during the register"
        }

def login(username, password):
    try:
        query = "SELECT id FROM TBL_USERS WHERE username = %s AND PASSWORD = %s"
        
        passwordHashed = pwsEncription.hashPassword(password)
        
        values = (username, passwordHashed)
        conn.execute(query, values)
        conn.commit()
        
        return {
            "status": "ok",
            "response": "Login successfully"
        }
        
    except Exception as error:
        conn.rollback()
        print(error)
        return {
            "status": "error",
            "response": "An error has occurred during the login"
        }
    