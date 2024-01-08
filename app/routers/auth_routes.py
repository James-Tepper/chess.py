import re
import secrets
from datetime import datetime, timedelta
from typing import Dict, TypedDict
from uuid import uuid4

from fastapi import APIRouter, Cookie, HTTPException, status, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, validator

import app.security as security
from app import settings
from app.dtos.accounts import AccountDTO
from app.dtos.sessions import SessionDTO
from app.privileges import Privileges
from app.schemas import accounts, sessions
from app.schemas.accounts import Account
from app.session_access import SessionAccess

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
async def login(login_info: Dict[str, str]) -> JSONResponse:
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

    expires_delta = datetime.now() + timedelta(days=1)
    expires_delta_seconds = int(timedelta(days=1).total_seconds())

    session_response = SessionDTO(
        session_id=session["session_id"],
        account_id=session["account_id"],
        created_at=session["created_at"],
        expires_at=expires_delta,
        status=SessionAccess.GRANTED,
        data=session["data"],
    )

    token_response = security.create_access_token(
        data={
            "sub": account["username"],
            "account_id": str(account["account_id"]),
            "session_id": str(session["session_id"]),
        },
        secret_key=settings.SECRET_KEY,
        expires_delta=expires_delta,
    )

    response = JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"session": session_response, "token": token_response}
    )

    response.set_cookie(
        key="token",
        value=token_response,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=expires_delta_seconds,
    )

    return response


@router.delete("/logout")
async def logout(response: Response, token: str = Cookie(...)) -> Response:
    invalid_token = await security.invalidate_token(token)

    if invalid_token:
        response.set_cookie(
            key="token",
            value="",
            httponly=True,
            secure=True,
            samesite="strict",
            max_age=0
        )

    return response
