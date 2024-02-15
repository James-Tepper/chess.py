from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Dict
from app.session_access import SessionAccess

class SessionDTO(BaseModel):
    session_id: UUID
    account_id: int
    token_id: str
    created_at: datetime
    expires_delta: datetime
    access: SessionAccess
    data: Dict[str, str] | None



