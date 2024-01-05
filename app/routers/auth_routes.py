import re
import secrets
from datetime import datetime, timedelta
from typing import Dict, Literal, TypedDict
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, validator

import app.security as security
from app.dtos.accounts import AccountDTO
from app.dtos.sessions import SessionDTO
from app.privileges import Privileges
from app.schemas import accounts, sessions
from app.schemas.accounts import Account

router = APIRouter()


class LoginResponse(TypedDict):
    session: SessionDTO
    token: str


class AccountRegistration(BaseModel):
    username: str
    email_address: EmailStr
    password: str
    country: str

    @validator("username")
    def validate_username(cls, username):
        if not re.match(r"^[a-zA-Z0-9_]{3,30}$", username):
            raise ValueError("Invalid username")
        return username

    @validator("password")
    def validate_password(cls, password):
        if len(password) < 8:
            raise ValueError("Invalid password")
        return password


@router.post("/register")
async def register(user: AccountRegistration) -> AccountDTO:
    """
    Used exclusively for USER registration only
    """
    username_available = await accounts.check_username_availability(user.username)

    if not username_available:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    hashed_password = security.hash_password(user.password)

    account: Account = await accounts.create(
        username=user.username,
        email_address=user.email_address,
        password=hashed_password,
        privileges=Privileges.USER,
        country=user.country,
    )

    response = AccountDTO(
        account_id=account["account_id"],
        username=account["username"],
        email_address=account["email_address"],
        country=account["country"],
        wins=account["wins"],
        loses=account["loses"],
        draws=account["draws"],
        win_rate=account["win_rate"],
        games_played=account["games_played"],
    )

    return response


@router.get("/login")
async def login(login_info: Dict[str, str]) -> LoginResponse:
    username = login_info.get("username")
    password = login_info.get("password")

    if not username or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username & password must be provided",
        )

    account = await accounts.fetch_by_username(username)

    assert account is not None

    if not security.check_password(password, account["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Credentials"
        )

    session = await sessions.create(
        session_id=uuid4(), account_id=account["account_id"]
    )

    expires_delta = datetime.now() + timedelta(minutes=30)

    session_response = SessionDTO(
        session_id=session["session_id"],
        account_id=session["account_id"],
        created_at=session["created_at"],
        expires_at=expires_delta,
        data=session["data"],
    )

    token_secret = secrets.token_hex(32)

    token_response = security.create_access_token(
        data={"sub": account["username"]},
        secret_key=token_secret,
        expires_delta=expires_delta,
    )

    response: LoginResponse = {"session": session_response, "token": token_response}

    return response
