from datetime import datetime
from typing import Dict, TypedDict, cast
from uuid import UUID

from app import clients

READ_PARAMS = """
    session_id,
    account_id,
    created_at,
    expires_at,
    data
"""


class Session(TypedDict):
    session_id: UUID
    account_id: int
    created_at: datetime
    expires_at: datetime
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
