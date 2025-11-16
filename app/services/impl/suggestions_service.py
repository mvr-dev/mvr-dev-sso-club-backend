from data.repositories.IUserRepository import IUserRepository
from ..isuggestions_service import ISuggestionsService


class SuggestionsService(ISuggestionsService):

    def __init__(self, userRepository: IUserRepository):
        self.userRepository = userRepository
        self._names = None
        self._surnames = None

    async def getNames(self,prefix:str):
        if self._names is None:
            users = await self.userRepository.getAllUsers()
            # print(users)
            self._names =set([user.name for user in users])
        return list(filter(lambda x: x.lower().startswith(prefix.lower()),self._names))
    
    async def getSurnames(self,prefix):
        if self._surnames is None:
            users = await self.userRepository.getAllUsers()
            # print(users)
            self._surnames =set([user.surname for user in users])
            # print(self._surnames)
        return list(filter(lambda x: x.lower().startswith(prefix.lower()),self._surnames))