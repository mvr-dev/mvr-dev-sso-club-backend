from typing import Optional,List
from data.models.db_models.db_account import Account as DbAccount
from data.models.account import Account
from data.repositories.iaccount_repository import IAccountRepository
from sqlalchemy.orm import Session

class AccountRepository(IAccountRepository):
    def __init__(self,db:Session):
        self.db = 
    
    async def getAccountById(self, id : int) -> Optional[Account]: 
        pass

    async def getAllAccounts(self) -> List[Account]: 
        pass

    async def addAccount(self,account:Account) -> Account:
        pass

    async def updateAccount(self, account: Account)-> Account:
        pass

    async def deleteAccount(self, id: int):
        pass