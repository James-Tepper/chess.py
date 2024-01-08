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


class AccountUpdateDTO(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    country: str | None = None
    wins: int | None = None
    loses: int | None = None
    draws: int | None = None
    win_rate: float | None = None
    games_played: int | None = None
