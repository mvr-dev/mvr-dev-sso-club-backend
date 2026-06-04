from datetime import datetime, timezone

from data.models.membership import Membership
from data.models.response.community_responce import CommunityResponce
from data.models.community import Community
from data.models.create_request.community_create_request import CommunityCreateRequest
from data.models.enums.community_status_enum import CommunityStatus
from data.models.update_request.community_update_request import CommunityUpdateRequest
from services.imembership_service import IMembershipService
from data.repositories.icommunity_repository import ICommunityRepository
from services.icommunity_service import ICommunityService


class CommunityService(ICommunityService):
    def __init__(self, repository: ICommunityRepository
                 #,membershipService: IMembershipService
                 ):
        self._repository = repository
        #self._membershipService = membershipService
    
    async def getAllCommunity(self):
        communities = await self._repository.getAllCommunity()
        return [CommunityResponce(
            community_id=community_res.community_id,
            community_type=community_res.community_type,
            name=community_res.name,
            purpose=community_res.purpose,
            status=community_res.status) for community_res in communities]
    
    async def getCommuntyByID(self, id: int):
        community_res = await self._repository.getCommuntyByID(id)
        if community_res is not None:
            return CommunityResponce(
                community_id=community_res.community_id,
                community_type=community_res.community_type,
                name=community_res.name,
                purpose=community_res.purpose,
                status=community_res.status)
        raise FileNotFoundError("Community with id: {id} not found")
    
    async def addCommunity(self, communityCreateRequest: CommunityCreateRequest):
        community = Community(
            community_type=communityCreateRequest.community_type,
            name=communityCreateRequest.name,
            purpose=communityCreateRequest.purpose,
            status=CommunityStatus.DRAFT.value,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        community_res =  await self._repository.addCommunity(community)
        return CommunityResponce(
            community_id=community_res.community_id,
            community_type=community_res.community_type,
            name=community_res.name,
            purpose=community_res.purpose,
            status=community_res.status)
    
    #TODO
    async def updateCommunity(self,communityUpdateRequest:CommunityUpdateRequest):
        community = Community(
            community_type=communityUpdateRequest.community_type,
            name=communityUpdateRequest.name,
            purpose=communityUpdateRequest.name,
            status=communityUpdateRequest.status,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        updatedCommunity =  await self._repository.updateCommunity(community)
        #membership = Membership()
    async def deleteCommunity(self, id):
        pass
    
    