from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Index, Integer
from sqlalchemy.orm import relationship

from app.data.models.enums.membership_type_enum import MembershipType
from core.database import Base


class Membership(Base):
    __tablename__ = "membership"
    __table_args__ = (
        CheckConstraint(
            "(status = 'left' AND left_at IS NOT NULL) OR (status <> 'left')",
            name="ck_membership_left_at"
        ),
        Index(
            "ux_membership_active", 
            "person_id", "community_id", 
            unique=True,
            postgresql_where=(Column("status") == "active")
        ),
    )

    membership_id = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    person_id = Column(
        Integer, 
        ForeignKey("person.person_id", ondelete="CASCADE"), 
        nullable=False
    )
    community_id = Column(
        Integer, 
        ForeignKey("community.community_id", ondelete="CASCADE"), 
        nullable=False
    )
    joined_at = Column(
        DateTime(timezone=True), 
        nullable=False, 
        default=datetime.datetime.now(timezone.utc)
    )
    status = Column(
        Enum(MembershipType), 
        nullable=False, 
        default=MembershipType.ACTIVE
    )
    left_at = Column(
        DateTime(timezone=True), 
        nullable=True
    )

    # Relationships
    person = relationship(
        "Person", 
        back_populates="memberships",
        lazy="selectin"
    )
    community = relationship(
        "Community", 
        back_populates="memberships",
        lazy="selectin"
    )