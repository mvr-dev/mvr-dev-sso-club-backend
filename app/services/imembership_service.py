from abc import ABC, abstractmethod

from data.models.membership import Membership


class IMembershipService(ABC):
    @abstractmethod
    async def getmembershipByID(self,id :int) -> Membership:
        pass

    @abstractmethod
    async def getAllMembership(self) -> list[Membership]:
        pass

    @abstractmethod
    async def addMembership(self,user_id, community_id)->Membership:
        pass

    @abstractmethod
    async def updateMembership(self,membership:Membership)->Membership:
        pass

    @abstractmethod
    async def deleteMembership(self,id:int):
        pass
