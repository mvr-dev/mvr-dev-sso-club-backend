import uuid

from fastapi import Depends, HTTPException, status
from api import dependensies
from data.models.update_request.user_update_request import UserUpdateRequest
from services.auth.utils import validate_password
from services.iaccount_service import IAccountService
from data.repositories.iuser_repository import IUserRepository
from data import UserResponse, UserCreateRequest
from data.models.user import Credentials, User
from ..iuser_service import IUserService

class UserService(IUserService):
    def __init__(self, userRepository: IUserRepository, accountService: IAccountService):
        self._userRepository = userRepository
        self._accountService = accountService
    
    # async def getAllUsers(self):
    #     self._userRepository.getAllUsers()
    async def getUserById(self,id:int)->UserResponse:
        saved_user = await self._userRepository.getUserById(id) 
        if saved_user !=None:
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
        raise FileNotFoundError(f"User with id {id} not found")
    
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
        saved_user = await self._userRepository.addUser(user)
        account = await self._accountService.addAccount(user_id=saved_user.id,
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
    async def validate_user(self,creds : Credentials):
        unauthorized_exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='invalid login or password')
        if not (account := await self._accountService.getAccountByLogin(creds.login)):
            print('no auth')
            raise unauthorized_exc
        if validate_password(creds.password,account.password):
            print('auth')
            return self.getUserById(account.user_id)
        raise unauthorized_exc
    
    async def updateUser(self,id:int ,userUpdateRequest: UserUpdateRequest, userToUpdate: UserResponse):
        user = User(id = None,
                    surname = userUpdateRequest.surname,
                    name = userUpdateRequest.name,
                    patronymic=userUpdateRequest.patronymic,
                    phone=userUpdateRequest.phone,
                    birthday=userUpdateRequest.birthday,
                    region=userUpdateRequest.region,
                    city=userUpdateRequest.city,
                    street=userUpdateRequest.street,
                    house=userUpdateRequest.house,
                    email=userToUpdate.email,
                    user_code=None
                    )
        saved_user = await self._userRepository.updateUser(id,user)
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
    
    async def deleteUser(self,id:int):
        await self._userRepository.deleteUser(id)
    