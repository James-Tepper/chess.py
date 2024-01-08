from datetime import datetime
from typing import Dict, List, TypedDict, cast
from uuid import UUID

from app import clients

READ_PARAMS = """
    session_id,
    account_id,
    created_at,
    expires_at,
    access,
    data
"""

# TODO implement status in db

class Session(TypedDict):
    session_id: UUID
    account_id: int
    created_at: datetime
    expires_at: datetime
    access: bool
    data: Dict[str, str] | None


async def create(
    session_id: UUID,
    account_id: int,
) -> Session:
    session = await clients.database.fetch_one(
        query=f"""
            INSERT INTO sessions
            (session_id, account_id)
            VALUES (:session_id, :account_id)
            RETURNING {READ_PARAMS}
            """,
        values={"session_id": session_id, "account_id": account_id},
    )
    assert session is not None
    return cast(Session, session)


async def delete_by_account_id(account_id: int) -> List[Session]:
    sessions = await clients.database.fetch_all(
        query=f"""
        DELETE FROM sessions
        WHERE account_id = :account_id
        RETURNING {READ_PARAMS}
        """,
        values={"account_id": account_id},
    )
    return cast(List[Session], sessions)


async def fetch_by_id(session_id: UUID) -> Session | None:
    session = await clients.database.fetch_one(
        query=f"""
            SELECT {READ_PARAMS}
            FROM sessions
            WHERE session_id = :session_id
        """,
        values={"session_id": session_id},
    )
    return cast(Session, session) if session is not None else None
