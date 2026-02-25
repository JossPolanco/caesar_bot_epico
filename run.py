from flask import Flask, request, jsonify
from encryption import encryption, decryption

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)