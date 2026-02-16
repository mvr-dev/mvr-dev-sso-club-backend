from abc import ABC, abstractmethod
from typing import Optional,List
from data.models.account import Account

class IAccountRepository(ABC):
    @abstractmethod
    async def getAccountById(self, id : int) -> Optional[Account]: # type: ignore
        pass

    @abstractmethod 
    async def getAllAccounts(self) -> List[Account]: # type: ignore
        pass

    @abstractmethod
    async def addAccount(self,account:Account) -> Account:
        pass

    @abstractmethod
    async def updateAccount(self, account: Account)-> Account:
        pass

    @abstractmethod
    async def deleteAccount(self, id: int):
        pass