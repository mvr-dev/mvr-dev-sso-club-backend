from data.models.account import Account
from data.repositories.iaccount_repository import IAccountRepository
from services.iaccount_service import IAccountService


class AccountService(IAccountService):
    def __init__(self, accountRepository: IAccountRepository):
        self.accountRepository = accountRepository

    async def addAccount(self, user_id, password, email) -> Account:
        account = Account(user_id=user_id,login=email,password=password,status=2)
        return await self.accountRepository.addAccount(account=account)
        