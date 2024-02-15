from datetime import datetime
from typing import List, TypedDict, cast
from app.dtos.piece import PieceDTO
from app import clients
from app.game_types import GameType

READ_PARAMS = """
    game_id,
    white_account_id,
    black_account_id,
    game_type,
    active,
    encoded_pieces,
    start_time,
    end_time
"""


class Game(TypedDict):
    game_id: int
    white_account_id: int
    black_account_id: int
    game_type: GameType
    # TODO bonus time per move
    active: bool
    encoded_pieces: str # TODO figure out how to store
    start_time: datetime
    end_time: datetime


async def create(
    white_account_id: int,
    black_account_id: int,
    game_type: GameType,
) -> Game:
    game = await clients.database.fetch_one(
        query=f"""
            INSERT INTO games
            (white_account_id, black_account_id, game_type)
            VALUES (:white_account_id, :black_account_id, :game_type)
            RETURNING {READ_PARAMS}
            """,
        values={
            "white_account_id": white_account_id,
            "black_account_id": black_account_id,
            "game_type": game_type,
        },
    )
    assert game is not None
    return cast(Game, game)


async def fetch_by_id(game_id: int) -> Game | None:
    game = await clients.database.fetch_one(
        query=f"""
        SELECT {READ_PARAMS}
        FROM games
        WHERE game_id = :game_id
        """,
        values={
            "game_id": game_id
        }
    )
    assert game is not None
    return cast(Game, game) if game is not None else None


async def fetch_all() -> List[Game]:
    games = await clients.database.fetch_all(
        query=f"""
        SELECT {READ_PARAMS}
        FROM games
        """,
    )
    assert games is not None
    return cast(List[Game], games)


async def fetch_all_current() -> List[Game]:
    games = await clients.database.fetch_all(
        query=f"""
        SELECT {READ_PARAMS}
        FROM games
        WHERE active = True
        """,
    )
    assert games is not None
    return cast(List[Game], games)
