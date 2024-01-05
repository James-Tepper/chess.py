from datetime import datetime, timedelta
from typing import Dict
from app.settings import SECRET_KEY
import jwt
from bcrypt import checkpw, gensalt, hashpw


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed_password = hashpw(password_bytes, gensalt())

    return hashed_password.decode("utf-8")


def check_password(password: str, hashed_password: str) -> bool:
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = hashed_password.encode("utf-8")

    return checkpw(password_bytes, hashed_password_bytes)


def create_access_token(
    data: Dict[str, str],
    secret_key: str = SECRET_KEY,
    expires_delta: timedelta = timedelta(minutes=15),
) -> str:
    shallow_data = data.copy()
    expire = datetime.utcnow() + expires_delta

    shallow_data.update({"exp": expire})
    encoded_jwt = jwt.encode(shallow_data, secret_key)

    return encoded_jwt
