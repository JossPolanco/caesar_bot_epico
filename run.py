from flask import Flask, request, jsonify
from encryption import encryption, decryption
from connection import createUser, login

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt_endpoint():
    data = request.json
    phrase = data.get('phrase')
    shift = data.get('shift')
    
    if not phrase or shift is None:
        return jsonify({'error': 'Missing phrase or shift'}), 400
    
    result = encryption(phrase, int(shift))
    
    return jsonify({'encrypted': result})

@app.route('/decrypt', methods=['POST'])
def decrypt_endpoint():
    data = request.json
    phrase = data.get('phrase')
    shift = data.get('shift')
    
    if not phrase or shift is None:
        return jsonify({'error': 'Missing phrase or shift'}), 400
    
    result = decryption(phrase, int(shift))
    
    return jsonify({'decrypted': result})

@app.route('/register', methods=['POST'])
def register_endpoint():
    data = request.json
    phoneNumber = str(data.get('phoneNumber'))
    password = data.get('password')
    
    if not phoneNumber or password is None:
        return jsonify({'error': 'Missing password'}), 400
    
    result = createUser(phoneNumber, password)
     
    if result['status'] == "ok": # type: ignore
        return jsonify({
            'status': "ok",
            'message': result['response'] # type: ignore
        })
    else:
        return jsonify({'error': result['response']}), 400 # type: ignore
        

@app.route('/login', methods=['POST'])
def login_endpoint():
    data = request.json
    phoneNumber = str(data.get('phoneNumber'))
    password = data.get('password')
    
    if not phoneNumber or password is None:
        return jsonify({'error': 'Missing password'}), 400
    
    result = login(phoneNumber, password)
    
    if result['status'] == "ok": # type: ignore
        return jsonify({
            'status': "ok",
            'message': result['response'], # type: ignore
            'phone': phoneNumber
        })
    else:
        return jsonify({'error': result['response']}), 400 # type: ignore

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)