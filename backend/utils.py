from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_pwd:str, hashed_pwd:str):
    return pwd_context.verify(plain_pwd, hashed_pwd)