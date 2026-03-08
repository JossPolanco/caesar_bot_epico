# Caesar Bot Epico

WhatsApp bot that encrypts and decrypts messages
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

### 3) Database installation
Run the following SQL in your PostgreSQL database:

```sql
CREATE TABLE TBL_USERS(
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        active BOOLEAN DEFAULT TRUE
);
```

## Execute
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

