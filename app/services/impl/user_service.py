from data.repositories import iuser_repository
from data import UserResponse, UserCreateRequest
from data.models.user import User
from ..iuser_service import IUserService

class UserService(IUserService):
    def __init__(self, userRepository: iuser_repository):
        self._userRepository = userRepository
    
    # async def getAllUsers(self):
    #     self._userRepository.getAllUsers()
    async def getUserById(self,id:int)->UserResponse:
        user = await self._userRepository.getUserById(id) 
        return UserResponse(
            id = user.id,
            name = user.name,
            surname = user.surname,
            patronymic= user.patronymic,
            email= user.email
        )
    
    async def addUser(self, userCreateRequest: UserCreateRequest) -> UserResponse:
        user = User(id = None,
                    surname = userCreateRequest.surname,
                    name = userCreateRequest.name,
                    patronymic=userCreateRequest.patronymic,
                    password = userCreateRequest.password,
                    email=userCreateRequest.email
                    )
        saved_user = await self._userRepository.addUser(user)
        return UserResponse(
            id = saved_user.id,
            name = saved_user.name,
            surname = saved_user.surname,
            patronymic= saved_user.patronymic,
            email= saved_user.email
        )