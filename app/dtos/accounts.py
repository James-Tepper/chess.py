from pydantic import BaseModel

class AccountDTO(BaseModel):
    account_id: int
    username: str
    email_address: str
    country: str
    wins: int
    loses: int
    draws: int
    win_rate: float
    games_played: int
