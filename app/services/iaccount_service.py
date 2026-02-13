from abc import ABC, abstractmethod

from data.models.account import Account

class IAccountService(ABC):
    @abstractmethod
    def addAccount(self,user_id:int,password:str,email:str) -> Account:
        pass

    def getAccountById(self, id:int) -> Account:
        pass