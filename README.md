# Caesar Bot Epico

Bot de WhatsApp que cifra y descifra mensajes
## Instalation
### 1) Python (Flask)
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### 2) Node.js (bot)
```bash
npm install
```

## Ejecutar
Open two terminals in the root of the project

Terminal A (Flask):
```bash
env\Scripts\activate
python run.py
```

Terminal B (bot):
```bash
node index.js
```

## Usage
- Encrpyt: `!cypher MENSSAGE SHIFT`
- Decrypt: `!decypher MENSSAGE SHIFT`

Examples:
- `!cypher HOLA 3`
- `!decypher KROD 3`

