from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from data.models.enums.membership_type_enum import MembershipType


class MembershipResponse(BaseModel):
    """Модель для ответа с данными членства"""
    membership_id: int
    person_id: int
    community_id: int
    joined_at: datetime
    status: MembershipType
    left_at: Optional[datetime] = None