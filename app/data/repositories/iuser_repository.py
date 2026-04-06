from abc import ABC, abstractmethod
from typing import Optional,List
from data.models.user import User

class IUserRepository(ABC):
    @abstractmethod
    async def getUserById(self, id : int) -> Optional[User]: # type: ignore
        pass

    @abstractmethod 
    async def getAllUsers(self) -> List[User]: # type: ignore
        pass

    @abstractmethod
    async def addUser(self,user:User) -> User:
        pass

    @abstractmethod
    async def updateUser(self,id:int ,user: User)-> User:
        pass

    @abstractmethod
    async def deleteUser(self, id: int):
        pass
