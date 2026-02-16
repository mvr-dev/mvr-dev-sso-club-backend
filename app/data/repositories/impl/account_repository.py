from typing import Optional,List
from data.models.db_models.db_account import Account as DbAccount
from data.models.account import Account
from data.repositories.iaccount_repository import IAccountRepository
from sqlalchemy.orm import Session

class AccountRepository(IAccountRepository):
    def __init__(self,db:Session):
        self.db = db
    
    async def getAccountById(self, id : int) -> Optional[Account]: 
        account = self.db.query(DbAccount).filter(DbAccount.id==id).first()
        #class Account(BaseModel):
        # id : int | None = None
        # user_id : int
        # organization_code : str
        # login : str
        # password : str
        # registration_date : date = date.today
        # status : int
        if account is not None:
            return Account(id = account.id,
                           user_id= account.user_id,
                           organization_code=account.organization_code,
                           login=account.login,
                           registration_date=account.registration_date,
                           status=account.status)
        else:
            raise FileNotFoundError(f"Account with id = {id} not found")

    async def getAllAccounts(self) -> List[Account]: 
        accounts = self.db.query(DbAccount).all()
        return [Account(id = account.id,
                           user_id= account.user_id,
                           organization_code=account.organization_code,
                           login=account.login,
                           registration_date=account.registration_date,
                           status=account.status) for account in accounts]

    async def addAccount(self,account:Account) -> Account:
        db_account = DbAccount(user_id = account.user_id,
                               organization_code = account.organization_code,
                               login = account.login,
                               password = account.password,
                               registration_date = account.registration_date,
                               status = account.status)
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return Account(id=db_account.id,
                       user_id= db_account.user_id,
                       organization_code=db_account.organization_code,
                       login=db_account.login,
                       password= db_account.password,
                       registration_date= db_account.registration_date,
                       status=db_account.status)
         

    async def updateAccount(self, account: Account)-> Account:
        pass

    async def deleteAccount(self, id: int):
        pass