import bcrypt

class PswEncription:
    def __init__(self) -> None:
        pass
    
    def hashPassword(self, password):
        password = password.encode("utf-8")
        pwdHashed = bcrypt.hashpw(password, bcrypt.gensalt())
        
        return pwdHashed
    
    # def verifyHashed(password):
    #     if bcrypt.checkpw(password, hashed):