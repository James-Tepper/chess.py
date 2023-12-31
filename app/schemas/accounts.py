from datetime import datetime
from typing import cast, TypedDict, List

from app import clients
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
    game_history,
    created_at,
    updated_at
"""

class Account(TypedDict):
    account_id: int
    username: str
    email_address: str
    password: str
    privileges: int
    country: str
    wins: int
    loses: int
    draws: int
    win_rate: float
    game_history: List[Game]
    created_at: datetime
    updated_at: datetime


async def create(



):
    ...
