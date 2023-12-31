from datetime import datetime
from typing import cast, TypedDict, List
from app.game_types import GameType
from app import clients

READ_PARAMS = """
    game_id,
    white_account_id,
    black_account_id,




"""


class Game(TypedDict):
    game_id: int
    white_account_id: int
    black_account_id: int
    game_type: GameType
    # TODO bonus time per move
    start_time: datetime
    end_time: datetime




