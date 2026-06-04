from datetime import datetime, timezone
from fastapi import HTTPException

from sqlalchemy.orm import Session

from data.repositories.imembership_repository import IMembershipRepository
from data.models.db_models.db_membership import Membership as DbMembersip
from data.models.membership import Membership
from data.models.enums.membership_type_enum import MembershipType


class MembershipRepository(IMembershipRepository):
    def __init__(self, db: Session):
        self._db = db

    async def getAllMembership(self):
        memberships = self._db.query(DbMembersip).all()
        return [Membership(
            membership_id=db_membership.membership_id,
            community_id=db_membership.community_id,
            person_id=db_membership.person_id,
            joined_at=db_membership.joined_at,
            status=db_membership.status,
            left_at=db_membership.left_at
        ) for db_membership in memberships]

    async def getmembershipByID(self, id):
        db_membership = self._db.query(DbMembersip).filter(DbMembersip.membership_id == id).one_or_none()
        if db_membership is not None:
            return Membership(
                membership_id=db_membership.membership_id,
                community_id=db_membership.community_id,
                person_id=db_membership.person_id,
                joined_at=db_membership.joined_at,
                status=db_membership.status,
                left_at=db_membership.left_at)
        else:
            raise FileNotFoundError("membership with id: {id} not found")

    async def addMembership(self, membership):
        db_membership = DbMembersip(
            person_id=membership.person_id,
            community_id=membership.community_id,
        )
        self._db.add(db_membership)
        self._db.commit()
        self._db.refresh(db_membership)
        return Membership(
            membership_id=db_membership.membership_id,
            community_id=db_membership.community_id,
            person_id=db_membership.person_id,
            joined_at=db_membership.joined_at,
            status=db_membership.status,
            left_at=db_membership.left_at)

    async def updateMembership(self, membership):
        db_membership = self._db.query(DbMembersip).filter(
            DbMembersip.membership_id == membership.membership_id
        ).one_or_none()
        
        if db_membership is None:
            raise HTTPException(
                status_code=404, 
                detail=f"Membership with id {membership.membership_id} not found"
            )
        
        # Обновляем поля в соответствии с входным параметром
        db_membership.person_id = membership.person_id
        db_membership.community_id = membership.community_id
        db_membership.status = membership.status
        db_membership.joined_at = membership.joined_at
        db_membership.left_at = membership.left_at
        
        self._db.commit()
        self._db.refresh(db_membership)
        
        return Membership(
            membership_id=db_membership.membership_id,
            community_id=db_membership.community_id,
            person_id=db_membership.person_id,
            joined_at=db_membership.joined_at,
            status=db_membership.status,
            left_at=db_membership.left_at
        )

    async def deleteMembership(self, id):
        db_membership = self._db.query(DbMembersip).filter(
            DbMembersip.membership_id == id
        ).one_or_none()
        
        if db_membership is None:
            raise HTTPException(
                status_code=404, 
                detail=f"Membership with id {id} not found"
            )
        
        # Устанавливаем статус "leaved" и время выхода
        db_membership.status = MembershipType.LEFT
        db_membership.left_at = datetime.now(timezone.utc)
        
        self._db.commit()
        self._db.refresh(db_membership)
        
        return Membership(
            membership_id=db_membership.membership_id,
            community_id=db_membership.community_id,
            person_id=db_membership.person_id,
            joined_at=db_membership.joined_at,
            status=db_membership.status,
            left_at=db_membership.left_at
        )