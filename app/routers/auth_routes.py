import re
from typing import TypedDict

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, validator

import app.security as security
from app.privileges import Privileges
from app.schemas import accounts
from app.schemas.accounts import Account

router = APIRouter()


class AccountRegistration(BaseModel):
    username: str
    email_address: EmailStr
    password: str
    privileges: Privileges
    country: str

    @validator("username")
    def validate_username(cls, username):
        if not re.match(r"^[a-zA-Z0-9_]{3,30}$", username):
            raise ValueError("Invalid credentials")
        return username

    @validator("password")
    def validate_password(cls, password):
        if len(password) < 8:
            raise ValueError("Invalid credentials")
        return password


@router.post("/register")
async def register(user: AccountRegistration) -> Account:
    """
    Used exclusively for USER registration only
    """
    if not user.privileges == Privileges.USER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    username_available = await accounts.check_username_availability(user.username)

    if not username_available:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    hashed_password = security.hash_password(user.password)

    account: Account = await accounts.create(
        username=user.username,
        email_address=user.email_address,
        password=hashed_password,
        privileges=user.privileges,
        country=user.country,
    )

    return account


@router.get("/login")
async def login():
    ...
