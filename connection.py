import psycopg
from flask import Flask, jsonify

conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="jpolanco4515#",
    port="5432"
)

def createUser(username, password):
    
    try:
        query = "INSERT INTO TBL_USERS (username, password) VALUES (%s, %s)"
        values = (username, password)
        conn.execute(query, values)
        conn.commit()
        
        return jsonify({
            "status": "ok",
            "response": "User successfully created"
        })
        
    except Exception as error:
        return jsonify({
            "status": "error",
            "response": error
        })
    
    