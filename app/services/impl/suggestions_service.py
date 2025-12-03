from data.repositories.iuser_repository import IUserRepository
from ..isuggestions_service import ISuggestionsService


class SuggestionsService(ISuggestionsService):

    def __init__(self, userRepository: IUserRepository):
        self.userRepository = userRepository
        self._names = set(["Виктор","Виталий","Владислав","Владлен"])
        self._surnames = set(["Иванов","Ивашкин","Ивлев","Ильев"])

    async def getNames(self,prefix:str):
        return list(filter(lambda x: x.lower().startswith(prefix.lower()),self._names))
    
    async def getSurnames(self,prefix):
        return list(filter(lambda x: x.lower().startswith(prefix.lower()),self._surnames))
    
    async def addName(self, name):
        self._names.add(name.capitalize())
    
    async def addSurname(self, surname):
        self._surnames.add(surname.capitalize())
    