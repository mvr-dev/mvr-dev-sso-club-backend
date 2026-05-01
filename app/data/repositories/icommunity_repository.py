from abc import ABC, abstractmethod

from data.models.community import Community


class ICommunityRepository(ABC):
    @abstractmethod
    async def getCommuntyByID(id :int) -> Community:
        pass

    @abstractmethod
    async def getAllCommunity() -> list[Community]:
        pass

    @abstractmethod
    async def addCommunity(community:Community)->Community:
        pass

    @abstractmethod
    async def updateCommunity(community:Community)->Community:
        pass

    @abstractmethod
    async def deleteCommunity(id:int):
        pass
