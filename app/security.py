from datetime import datetime, timedelta
from typing import Dict
from uuid import UUID

import jwt
from bcrypt import checkpw, gensalt, hashpw
from schemas import accounts, sessions

from app import settings


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
    secret_key: str,
    expires_delta: timedelta = timedelta(minutes=15),
) -> str:
    shallow_data = data.copy()
    expire = datetime.utcnow() + expires_delta

    shallow_data.update({"exp": expire})
    encoded_jwt = jwt.encode(shallow_data, secret_key)

    return encoded_jwt


INVALID_TOKENS = set()

async def invalidate_token(token: str) -> bool:
    payload: Dict[str, str] = jwt.decode(
        token, settings.SECRET_KEY, algorithms=["HS256"]
    )

    session = await sessions.fetch_by_id(UUID(payload["session_id"]))
    account = await accounts.fetch_by_id(int(payload["account_id"]))

    assert session is not None
    assert account is not None

    if not payload.get("session_id") == session["session_id"]:
        return False

    if not payload.get("sub") == account["username"]:
        return False

    INVALID_TOKENS.add(token)

    return True


def is_token_valid(token: str) -> bool:
    return token not in INVALID_TOKENS
