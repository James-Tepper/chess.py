from datetime import datetime
from typing import Dict, List, Literal, TypedDict, cast

from app import clients
from app.privileges import Privileges
from app.schemas.games import Game

READ_PARAMS = """
    account_id,
    username,
    email_address,
    privileges,
    password,
    country,
    wins,
    loses,
    draws,
    win_rate,
    games_played,
    created_at,
    updated_at
"""
# game_history,


class Account(TypedDict):
    account_id: int
    username: str
    email_address: str
    password: str
    privileges: Privileges
    country: str
    wins: int
    loses: int
    draws: int
    win_rate: float
    games_played: int
    # game_history: List[Game] TODO figure out
    created_at: datetime
    updated_at: datetime


async def create(
    username: str,
    email_address: str,
    password: str,
    privileges: int,
    country: str,
) -> Account:
    account = await clients.database.fetch_one(
        query=f"""
            INSERT INTO accounts
            (username, email_address, password, privileges, country)
            VALUES (:username, :email_address, :password, :privileges, :country)
            RETURNING {READ_PARAMS}
            """,
        values={
            "username": username,
            "email_address": email_address,
            "password": password,
            "privileges": privileges,
            "country": country,
        },
    )
    assert account is not None
    return cast(Account, account)


async def check_username_availability(
    username: str,
) -> bool:
    """
    True if username is taken
    """
    result = await clients.database.fetch_one(
        query=f"""
            SELECT username FROM accounts
            WHERE username = :username
            """,
        values={"username": username},
    )

    return result is None


async def update_win_or_loss_or_draw(
    account_id: int,
    win: bool | None = None,
    loss: bool | None = None,
    draw: bool | None = None,
) -> Account | None:
    """
    Updates Win | Loss | Draw
    Increments Total Games
    """
    if not win and not loss and not draw:
        raise AssertionError

    params = {
        k: v
        for k, v in {"win": win, "loss": loss, "draw": draw}.items()
        if v is not None
    }

    if len(params) > 1:
        raise AssertionError

    sql_query = "UPDATE accounts SET "

    for k, v in params.items():
        sql_query += f"{k} = :{k} + 1, "

    sql_query = sql_query[:-2]

    account = await clients.database.fetch_one(
        query=f"""{sql_query}
        RETURNING {READ_PARAMS}
        """,
        values=params,
    )

    return cast(Account, account) if account is not None else None


# Calculated post game
async def calculate_win_rate(
    account_id: int,
):
    ...
