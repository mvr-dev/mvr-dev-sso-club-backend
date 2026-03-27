# data/repositories/impl/account_repository.py
from typing import Optional, List
from data.models.db_models.db_account import Account as DbAccount
from data.models.account import Account
from data.repositories.iaccount_repository import IAccountRepository
from sqlalchemy.orm import Session

class AccountRepository(IAccountRepository):
    def __init__(self, db: Session):
        self.db = db
    
    async def getAccountById(self, id: int) -> Optional[Account]:
        account = self.db.query(DbAccount).filter(DbAccount.id == id).one_or_none()
        
        if account is not None:
            # Преобразуем password в bytes
            password_bytes = self._to_bytes(account.password)
            
            return Account(
                id=account.id,
                user_id=account.user_id,
                organization_code=account.organization_code,
                login=account.login,
                password=password_bytes,  # bytes
                registration_date=account.registration_date,
                status=account.status
            )
        else:
            raise FileNotFoundError(f"Account with id = {id} not found")

    async def getAllAccounts(self) -> List[Account]:
        accounts = self.db.query(DbAccount).all()
        result = []
        for account in accounts:
            password_bytes = self._to_bytes(account.password)
            result.append(Account(
                id=account.id,
                user_id=account.user_id,
                organization_code=account.organization_code,
                login=account.login,
                password=password_bytes,
                registration_date=account.registration_date,
                status=account.status
            ))
        return result

    async def addAccount(self, account: Account) -> Account:
        # account.password уже bytes после валидации Pydantic
        # Преобразуем bytes в memoryview или строку для SQLAlchemy
        db_account = DbAccount(
            user_id=account.user_id,
            organization_code=account.organization_code,
            login=account.login,
            password=account.password,  # bytes
            registration_date=account.registration_date,
            status=account.status
        )
        
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        
        # При возврате конвертируем обратно в bytes
        password_bytes = self._to_bytes(db_account.password)
        
        return Account(
            id=db_account.id,
            user_id=db_account.user_id,
            organization_code=db_account.organization_code,
            login=db_account.login,
            password=password_bytes,
            registration_date=db_account.registration_date,
            status=db_account.status
        )

    async def updateAccount(self, account: Account) -> Account:
        pass

    async def deleteAccount(self, id: int):
        pass

    async def getAccountByLogin(self, login: str):
        account = self.db.query(DbAccount).filter(DbAccount.login == login).first()
        if account:
            password_bytes = self._to_bytes(account.password)
            return Account(
                id=account.id,
                user_id=account.user_id,
                organization_code=account.organization_code,
                login=account.login,
                password=password_bytes,
                registration_date=account.registration_date,
                status=account.status
            )
        return None
    
    def _to_bytes(self, value):
        """Преобразует memoryview, str или bytes в bytes"""
        if value is None:
            return None
        if isinstance(value, memoryview):
            return bytes(value)
        if isinstance(value, str):
            return value.encode('utf-8')
        if isinstance(value, bytes):
            return value
        # Если что-то другое
        return bytes(value)