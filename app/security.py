from bcrypt import checkpw, gensalt, hashpw


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed_password = hashpw(password_bytes, gensalt())

    return hashed_password.decode("utf-8")


def check_password(password: str, hashed_password: str) -> bool:
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = hashed_password.encode("utf-8")

    return checkpw(password_bytes, hashed_password_bytes)
