from typing import Optional,List
from data.models.db_models.db_user import User as DbUser
from data.models.user import User as UserModel
from data.repositories.iuser_repository import IUserRepository
from sqlalchemy.orm import Session

class UserRepository(IUserRepository):
    def __init__(self,db:Session):
        self.db = 
        # переделать создание модели в методах
    
    async def getUserById(self, id: int) -> Optional[UserModel]:
        # Исправлено: filter должен использовать сравнение ==
        foundUser = self.db.query(DbUser).filter(DbUser.id == id).first()
        if foundUser is not None:
            # Создаем UserModel, передавая параметры по порядку
            return UserModel(
                id=foundUser.id,
                surname=foundUser.surname,
                name=foundUser.name,
                patronymic=foundUser.patronymic,
                password=foundUser.hashed_password,  # Обратите внимание: в Pydantic модели поле называется password
                email=foundUser.email
            )
        else:
            raise FileNotFoundError(f"User with id {id} not found")

    async def getAllUsers(self) -> List[UserModel]:
        users = self.db.query(DbUser).all()
        return [
            UserModel(
                id=user.id,
                surname=user.surname,
                name=user.name,
                patronymic=user.patronymic,
                password=user.hashed_password,
                email=user.email
            ) for user in users
        ]

    async def addUser(self, user: UserModel) -> UserModel:
        # Создаем экземпляр DB модели
        db_user = DbUser(
            surname=user.surname,
            name=user.name,
            patronymic=user.patronymic,
            hashed_password=user.password,  # Сохраняем пароль как хэшированный
            email=user.email
        )
        
        # Добавляем в сессию и коммитим
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)  # Обновляем объект, чтобы получить ID
        
        # Возвращаем Pydantic модель с заполненным ID
        return UserModel(
            id=db_user.id,
            surname=db_user.surname,
            name=db_user.name,
            patronymic=db_user.patronymic,
            password=db_user.hashed_password,
            email=db_user.email
        )

        

    
    async def updateUser(self, user: UserModel)-> UserModel:
        pass

    
    async def deleteUser(self, id: int):
        pass