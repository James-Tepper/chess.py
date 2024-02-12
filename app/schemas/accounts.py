from datetime import datetime
from typing import Any, Dict, List, Literal, TypedDict, cast

from app import clients
from app.privileges import Privileges
from app.schemas import Outcome
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


async def fetch_all() -> List[Account]:
    accounts = await clients.database.fetch_all(
        query=f"""
        SELECT {READ_PARAMS}
        FROM accounts
        """,
    )
    assert accounts is not None
    return cast(List[Account], accounts)


async def fetch_by_id(account_id: int) -> Account | None:
    account = await clients.database.fetch_one(
        query=f"""
        SELECT {READ_PARAMS}
        FROM accounts
        WHERE account_id = :account_id
        """,
        values={
            "account_id": account_id,
        },
    )
    return cast(Account, account) if account is not None else None


async def fetch_many(
    privileges: int | None = None,
    page: int = 1,
    page_size: int = 50,
): ...


async def fetch_by_username(
    username: str,
) -> Account | None:
    account = await clients.database.fetch_one(
        query=f"""
            SELECT {READ_PARAMS}
            FROM accounts
            WHERE username = :username
            """,
        values={
            "username": username,
        },
    )
    return cast(Account, account) if account is not None else None


async def update(account_id: int, updates: Dict[str, Any]) -> Account | None:
    params = {k: v for k, v in updates.items() if v is not None}

    params["account_id"] = account_id

    conditions = [f"{k} = :{k}" for k in params.keys()]
    sql_query = f"UPDATE accounts SET {', '.join(conditions)}"

    account = await clients.database.fetch_one(
        query=f"""{sql_query}
        WHERE account_id = :account_id
        RETURNING {READ_PARAMS}
        """,
        values=params,
    )

    return cast(Account, account) if account is not None else None


async def check_username_availability(
    username: str,
) -> bool:
    # Returns True if username is taken
    result = await clients.database.fetch_one(
        query=f"""
            SELECT 1 FROM accounts
            WHERE username = :username
            """,
        values={"username": username},
    )

    return result is None


async def update_win_or_loss_or_draw(
    account_id: int, outcome: Outcome
) -> Account | None:
    """
    Updates Win | Loss | Draw
    Increments Total Games
    """
    sql_query = f"UPDATE accounts SET {outcome} = {outcome} + 1"

    account = await clients.database.fetch_one(
        query=f"""
        {sql_query}
        WHERE account_id = :account_id
        RETURNING {READ_PARAMS}
        """,
        values={
            "account_id": account_id,
        },
    )

    return cast(Account, account) if account is not None else None


# Calculated post game
async def calculate_win_rate(
    account_id: int,
): ...


async def delete_by_id(
    account_id: int,
) -> Account | None:
    account = await clients.database.fetch_one(
        query=f"""
            SELECT 1 FROM accounts
            WHERE account_id = :account_id
            """,
        values={
            "account_id": account_id,
        },
    )

    await clients.database.execute(
        query=f"""
            DELETE FROM accounts
            WHERE account_id = :account_id
            """,
        values={
            "account_id": account_id,
        },
    )

    return cast(Account, account) if account is not None else None


def get_account_info(
    game_dict: Dict[str, Any], color: Literal["white", "black"]
) -> Account:
    return cast(
        Account,
        {
            k.replace(f"{color}_", ""): v
            for k, v in game_dict.items()
            if k.startswith(f"{color}_")
        },
    )


async def fetch_account_by_game_id(
    game_id: int,
) -> Dict[Literal["white", "black"], Account]:
    game = await clients.database.fetch_one(
        query=f"""
        SELECT
        black.*,
        white.*
        FROM games
        INNER JOIN accounts AS black ON games.black_account_id = black.account_id
        INNER JOIN accounts AS white ON games.white_account_id = white.account_id
        WHERE games.game_id = :game_id
            """,
        values={"game_id": game_id},
    )

    assert game is not None

    game_dict = dict(game)

    white_account = get_account_info(game_dict, "white")
    black_account = get_account_info(game_dict, "black")

    accounts: Dict[Literal["white", "black"], Account] = {
        "white": white_account,
        "black": black_account,
    }

    return accounts
