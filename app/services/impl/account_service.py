from data.models.account import Account
from data.repositories.iaccount_repository import IAccountRepository
from services.iaccount_service import IAccountService
from services.auth.utils import hash_password


class AccountService(IAccountService):
    def __init__(self, accountRepository: IAccountRepository):
        self.accountRepository = accountRepository

    async def addAccount(self, user_id, password, email) -> Account:
        account = Account(user_id=user_id,login=email,password=hash_password(password),status=2)
        return await self.accountRepository.addAccount(account=account)
    
    async def getAccountById(self, id):
        return await self.accountRepository.getAccountById(id)
    
    async def getAccountByLogin(self, login):
        return await self.accountRepository.getAccountByLogin(login=login)