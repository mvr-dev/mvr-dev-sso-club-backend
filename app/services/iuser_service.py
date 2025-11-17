from abc import ABC, abstractmethod
from data.repositories import iuser_repository
from data import UserResponse, UserCreateRequest

class IUserService(ABC):        
    @abstractmethod
    async def getUserById(self,id:int)->UserResponse:
        pass
    
    @abstractmethod
    async def addUser(self, userCreateRequest: UserCreateRequest) -> UserResponse:
        pass
    