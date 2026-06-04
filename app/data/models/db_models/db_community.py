from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import Column, DateTime, Integer, String, Text, Enum as SqlEnum
from sqlalchemy.orm import relationship

from data.models.enums.community_status_enum import CommunityStatus
from data.models.enums.community_type_enum import CommunityType
from core.database import Base


class Community(Base):
    __tablename__ = "community"


    community_id = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    community_type = Column(
        SqlEnum(CommunityType), 
        nullable=False
    )
    name = Column(
        String(255), 
        nullable=False
    )
    purpose = Column(
        Text, 
        nullable=False
    )
    status = Column(
        SqlEnum(CommunityStatus), 
        nullable=False, 
        default=CommunityStatus.DRAFT.value
    )
    created_at = Column(
        DateTime(timezone=True), 
        nullable=False, 
        default=datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True), 
        nullable=False, 
        default=datetime.now(timezone.utc)
    )
