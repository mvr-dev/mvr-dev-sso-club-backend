import uuid
from services.iaccount_service import IAccountService
from data.repositories.iuser_repository import IUserRepository
from data import UserResponse, UserCreateRequest
from data.models.user import User
from ..iuser_service import IUserService

class UserService(IUserService):
    def __init__(self, userRepository: IUserRepository, accountService: IAccountService):
        self.userRepository = userRepository
        self.accountService = accountService
    
    # async def getAllUsers(self):
    #     self._userRepository.getAllUsers()
    async def getUserById(self,id:int)->UserResponse:
        saved_user = await self.userRepository.getUserById(id) 
        return UserResponse(
            id = saved_user.id,
            name = saved_user.name,
            surname = saved_user.surname,
            patronymic= saved_user.patronymic,
            email= saved_user.email,
            birthday=saved_user.birthday,
            region=saved_user.region,
            city=saved_user.city,
            street=saved_user.street,
            house=saved_user.house,
            phone=saved_user.phone
        )
    
    async def addUser(self, userCreateRequest: UserCreateRequest) -> UserResponse:
        user = User(id = None,
                    surname = userCreateRequest.surname,
                    name = userCreateRequest.name,
                    patronymic=userCreateRequest.patronymic,
                    phone=userCreateRequest.phone,
                    birthday=userCreateRequest.birthday,
                    region=userCreateRequest.region,
                    city=userCreateRequest.city,
                    street=userCreateRequest.street,
                    house=userCreateRequest.house,
                    user_code=str(uuid.uuid4())[:64],
                    email=userCreateRequest.email
                    )
        saved_user = await self.userRepository.addUser(user)
        account = await self.accountService.addAccount(user_id=saved_user.id,
                                                       password=userCreateRequest.password,
                                                       email=saved_user.email)
        return UserResponse(
            id = saved_user.id,
            name = saved_user.name,
            surname = saved_user.surname,
            patronymic= saved_user.patronymic,
            email= saved_user.email,
            birthday=saved_user.birthday,
            region=saved_user.region,
            city=saved_user.city,
            street=saved_user.street,
            house=saved_user.house,
            phone=saved_user.phone
        )