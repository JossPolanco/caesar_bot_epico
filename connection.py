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
        query = "SELECT id FROM TBL_USERS WHERE username = %s"        
        
        with conn.cursor() as cur:
            cur.execute(query, (username,))
            result = cur.fetchone()
        
        if result:
            return {
                "status": "error",
                "response": "User already exists"
            }
                
        query = "INSERT INTO TBL_USERS (username, password) VALUES (%s, %s)"
        
        passwordHashed = pwsEncription.hashPassword(password)
        
        if isinstance(passwordHashed, bytes):
            passwordHashed = passwordHashed.decode("utf-8")
            
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
        query = "SELECT password FROM TBL_USERS WHERE username = %s"
        
        with conn.cursor() as cur:
            cur.execute(query, (username,))
            result = cur.fetchone()
        
        if not result:
            return {
                "status": "error",
                "response": "User not found"
            }
            
        stored_hash = result[0]
        
        status = pwsEncription.verifyHashed(password, stored_hash)
        # Verificar la contraseña con bcrypt.checkpw
        if status == True:
            return {
                "status": "ok",
                "response": "Login successfully"
            }
        else:
            return {
                "status": "error",
                "response": "Invalid password"
            }
        
    except Exception as error:
        conn.rollback()
        print(error)
        return {
            "status": "error",
            "response": "An error has occurred during the login"
        }
    