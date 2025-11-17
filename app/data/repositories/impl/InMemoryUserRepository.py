from typing import Optional,List
from data.models.User import User
from data.repositories.iuser_repository import IUserRepository

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._data = {}
        self._next_id = 1
    
    async def getUserById(self, id : int) -> Optional[User]:
        return self._data.get(id)

     
    async def getAllUsers(self) -> List[User]:
        # print(self._data)
        return self._data.values()

    
    async def addUser(self,user:User) -> User:
        if user.id is None:
            user.id = self._next_id
            self._next_id+=1
        self._data[user.id] = user
        # print(user)
        return user

    
    async def updateUser(self, user: User)-> User:
        pass

    
    async def deleteUser(self, id: int):
        pass