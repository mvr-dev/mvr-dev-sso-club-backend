from abc import ABC, abstractmethod
from data.models.update_request.user_update_request import UserUpdateRequest
from data import UserResponse, UserCreateRequest

class IUserService(ABC):        
    @abstractmethod
    async def getUserById(self,id:int)->UserResponse:
        pass
    
    @abstractmethod
    async def addUser(self, userCreateRequest: UserCreateRequest) -> UserResponse:
        pass

    @abstractmethod
    async def updateUser(self, id: int, userUpdateRequest: UserUpdateRequest) -> UserResponse:
        pass
    