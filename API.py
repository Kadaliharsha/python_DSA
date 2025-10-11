import hashlib
import jwt
from datetime import datetime, timedelta

SECRET = "secret"
db = {}

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(email, password):
    if email in db:
        return "User exists"
    db[email] = hash_pw(password)
    return "User created"

