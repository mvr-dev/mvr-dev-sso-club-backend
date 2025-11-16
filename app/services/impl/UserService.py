from data.repositories import IUserRepository
from data import UserResponse, UserCreateRequest
from data.models.User import User
from ..iuser_service import IUserService

class UserService(IUserService):
    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository
    
    # async def getAllUsers(self):
    #     self._userRepository.getAllUsers()
    async def getUserById(self,id:int)->UserResponse:
        user = await self._userRepository.getUserById(id) 
        return UserResponse(user.id,user.name,user.surname)
    
    async def addUser(self, userCreateRequest: UserCreateRequest) -> UserResponse:
        user = User(id = None,
                    surname = userCreateRequest.surname,
                    name = userCreateRequest.name,
                    password = userCreateRequest.password)
        saved_user = await self._userRepository.addUser(user)
        return UserResponse(
            id = saved_user.id,
            name = saved_user.name,
            surname = saved_user.surname
        )