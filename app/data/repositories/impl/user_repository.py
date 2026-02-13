from typing import Optional,List
from data.models.db_models.db_user import User as DbUser
from data.models.user import User as UserModel
from data.repositories.iuser_repository import IUserRepository
from sqlalchemy.orm import Session

class UserRepository(IUserRepository):
    def __init__(self,db:Session):
        self.db = db
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
                email=foundUser.email,
                phone=foundUser.phone,
                region=foundUser.region,
                city=foundUser.city,
                street=foundUser.street,
                house=foundUser.house,
                clone_code=foundUser.clone_code,
                user_code=foundUser.user_code,
                birthday=foundUser.birthday
            )
        else:
            raise FileNotFoundError(f"User with id {id} not found")

    async def getAllUsers(self) -> List[UserModel]:
        users = self.db.query(DbUser).all()
        return [
            UserModel(
                id=foundUser.id,
                surname=foundUser.surname,
                name=foundUser.name,
                patronymic=foundUser.patronymic,
                email=foundUser.email,
                phone=foundUser.phone,
                region=foundUser.region,
                city=foundUser.city,
                street=foundUser.street,
                house=foundUser.house,
                clone_code=foundUser.clone_code,
                user_code=foundUser.user_code,
                birthday=foundUser.birthday
            ) for foundUser in users
        ]

    async def addUser(self, user: UserModel) -> UserModel:
        # Создаем экземпляр DB модели
        db_user = DbUser(
            id=user.id,
            surname=user.surname,
            name=user.name,
            patronymic=user.patronymic,
            email=user.email,
            phone=user.phone,
            region=user.region,
            city=user.city,
            street=user.street,
            house=user.house,
            clone_code=user.clone_code,
            user_code=user.user_code,
            birthday=user.birthday
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
                email=db_user.email,
                phone=db_user.phone,
                region=db_user.region,
                city=db_user.city,
                street=db_user.street,
                house=db_user.house,
                clone_code=db_user.clone_code,
                user_code=db_user.user_code,
                birthday=db_user.birthday
            )

        

    
    async def updateUser(self, user: UserModel)-> UserModel:
        pass

    
    async def deleteUser(self, id: int):
        pass