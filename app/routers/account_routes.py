from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

import app.security as security
from app.dtos.accounts import AccountDTO, AccountUpdateDTO
from app.schemas import accounts
from app import logger

router = APIRouter()



def filter_keys(obj: Dict[str, Any], exclude: List[str]) -> Dict[Any, Any]:
    return {k: v for k, v in obj.items() if k not in exclude}


@router.get("/")
async def get_all_accounts():
    all_accounts = await accounts.fetch_all()

    response = JSONResponse(
        status_code=status.HTTP_200_OK, content={"all_accounts": all_accounts}
    )

    return response


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
    try:
        await accounts.delete_by_id(account_id)
    except: # implement for all errors (as syntax)
        logger.info(
            "Account was unable to be deleted",
            extra=account_id
            )
        return False
