from abc import ABC, abstractmethod

from data.models.update_request.community_update_request import CommunityUpdateRequest
from data.models.create_request.community_create_request import CommunityCreateRequest
from data.models.community import Community


class ICommunityService(ABC):
    @abstractmethod
    async def getCommuntyByID(self,id :int) -> Community:
        pass

    @abstractmethod
    async def getAllCommunity(self) -> list[Community]:
        pass

    @abstractmethod
    async def addCommunity(self,community:CommunityCreateRequest)->Community:
        pass

    @abstractmethod
    async def updateCommunity(self,community:CommunityUpdateRequest)->Community:
        pass

    @abstractmethod
    async def deleteCommunity(self,id:int):
        pass
