from abc import ABC, abstractmethod
from services.iaccount_service import IAccountService
from data.models.user import Credentials
from data import UserResponse, UserCreateRequest

class IUserService(ABC):        
    @abstractmethod
    async def getUserById(self,id:int)->UserResponse:
        pass
    
    @abstractmethod
    async def addUser(self, userCreateRequest: UserCreateRequest) -> UserResponse:
        pass
    
    @abstractmethod
    def validate_user(self,creds : Credentials):
        pass
    
    