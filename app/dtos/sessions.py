from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Dict

class SessionDTO(BaseModel):
    session_id: UUID
    account_id: int
    created_at: datetime
    expires_at: datetime
    data: Dict[str, str] | None
