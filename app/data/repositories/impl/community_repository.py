from datetime import datetime, timezone
from typing import Optional

from sqlalchemy.orm import Session
from data.repositories.icommunity_repository import ICommunityRepository
from data.models.db_models.db_community import Community as DbCommunity
from data.models.community import Community


class CommunityRepository(ICommunityRepository):
    def __init__(self,db:Session):
        self._db = db
    
    async def getAllCommunity(self):
        communities = self._db.query(DbCommunity).all()
        return [Community(
            community_id = db_community.community_id,
            community_type=db_community.community_type,
            name=db_community.name,
            purpose=db_community.purpose,
            status = db_community.status,
            created_at=db_community.created_at,
            updated_at = db_community.updated_at 
        ) for db_community in communities]
    
    async def getCommuntyByID(self, id) -> Optional[Community]:
        db_community = self._db.query(DbCommunity).filter(DbCommunity.community_id==id).one_or_none()
        if db_community is not None:
            return Community(
            community_id = db_community.community_id,
            community_type=db_community.community_type,
            name=db_community.name,
            purpose=db_community.purpose,
            status = db_community.status,
            created_at=db_community.created_at,
            updated_at = db_community.updated_at)
    
    async def addCommunity(self,community):
        db_community = DbCommunity(
            community_type = community.community_type,
            name = community.name,
            purpose = community.purpose,
            status = community.status
        )
        self._db.add(db_community)
        self._db.commit()
        self._db.refresh(db_community)
        return Community(
            community_id = db_community.community_id,
            community_type=db_community.community_type,
            name=db_community.name,
            purpose=db_community.purpose,
            status = db_community.status,
            created_at=db_community.created_at,
            updated_at = db_community.updated_at)
    
    async def deleteCommunity(self, id):
        community = self._db.query(DbCommunity).filter(DbCommunity.community_id==id).one()
        self._db.delete(community)
        self._db.commit()
    
    async def updateCommunity(self, community):
        community_to_update = self._db.query(DbCommunity).filter(DbCommunity.community_id==community.community_id).first()
        if community_to_update is not None:
            community_to_update.community_type=community.community_type
            community_to_update.name = community.name
            community_to_update.purpose = community.purpose
            community_to_update.status = community.status
            community_to_update.updated_at = datetime.now(timezone.utc)
            self._db.commit()
            return Community(
                community_id = community_to_update.community_id,
                community_type=community_to_update.community_type,
                name=community_to_update.name,
                purpose=community_to_update.purpose,
                status = community_to_update.status,
                created_at=community_to_update.created_at,
                updated_at = community_to_update.updated_at)
        raise FileNotFoundError(f"community with id: {community.community_id} not found")
