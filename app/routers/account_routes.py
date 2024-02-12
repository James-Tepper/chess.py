from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

import app.security as security
from app.dtos.accounts import AccountDTO, AccountUpdateDTO
from app.schemas import accounts
from app.utils import filter_keys

router = APIRouter()

@router.get("/")
async def get_all_accounts():
    all_accounts = await accounts.fetch_all()

    # return response

@router.get("/{account_id}")
async def get_account(account_id: int) -> JSONResponse:
    account = await accounts.fetch_by_id(account_id)

    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    filtered_account = filter_keys(dict(account), exclude=["password"])

    response = JSONResponse(
        status_code=status.HTTP_200_OK, content={"account": filtered_account}
    )

    return response


@router.put("/{account_id}")
async def update_account(
    account_id: int, account_data: AccountUpdateDTO
) -> JSONResponse:
    """
    TODO implement change password later
    """
    # assert account_data.password is not None
    # hashed_password = security.hash_password(account_data.password)
    # await accounts.update(account_id, hashed_password: str)...
    account = await accounts.fetch_by_id(account_id)

    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    updated_account = await accounts.update(
        account_id, account_data.dict(exclude_unset=True)
    )

    if updated_account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    filtered_updated_account = filter_keys(dict(updated_account), exclude=["password"])

    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"account": filtered_updated_account}
    )


@router.delete("/{account_id}")
async def delete_account(account_id: int):
    return await accounts.delete_by_id(account_id)
