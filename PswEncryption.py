import bcrypt

class PswEncription:
    def __init__(self) -> None:
        pass
    
    def hashPassword(self, password):
        password = password.encode("utf-8")
        pwdHashed = bcrypt.hashpw(password, bcrypt.gensalt())
        
        return pwdHashed
    
    def verifyHashed(self, password, stored_hash):
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode("utf-8")
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash)