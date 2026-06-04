from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from data.models.enums.membership_type_enum import MembershipType


class MembershipUpdateRequest(BaseModel):
    """Модель для запроса на обновление членства"""
    membership_id: int
    person_id: Optional[int] = None
    community_id: Optional[int] = None
    status: Optional[MembershipType] = None
    joined_at: Optional[datetime] = None
    left_at: Optional[datetime] = None