from passlib.context import CryptContext
pwd_context = CryptContext(schemes = ["argon2"], deprecated = "auto")

def get_hash(password ):
    return pwd_context.hash(password)

def auth(plain_password , hashed_password):
    return pwd_context.verify(plain_password,hashed_password)