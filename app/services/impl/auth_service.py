from fastapi import HTTPException, status

from services.iaccount_service import IAccountService
from services.iuser_service import IUserService
from services.auth.utils import validate_password
from data.models.user import Credentials
from services.iauth_service import IAuthService


class AuthService(IAuthService):
    def __init__(self, userService: IUserService, accountService: IAccountService):
        self._userService = userService
        self._accountService = accountService
    async def validate_user(self,creds : Credentials):
        unauthorized_exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='invalid login or password')
        if not (account := await self._accountService.getAccountByLogin(creds.login)):
            print('no auth')
            raise unauthorized_exc
        if validate_password(creds.password,account.password):
            print('auth')
            return self._userService.getUserById(account.user_id)
        raise unauthorized_exc