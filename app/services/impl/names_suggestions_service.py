from data.repositories.iuser_repository import IUserRepository
from ..isuggestions_service import ISuggestionsService


class NamesSuggestionsService(ISuggestionsService):

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository
        self._names = set(["Виктор","Виталий","Владислав","Владлен"])

    async def getSuggestion(self, prefix):
        names_in_repo = set(map(lambda x: x.name, await self._userRepository.getAllUsers()))
        names = names_in_repo | self._names
        return set(filter(lambda x: x.startswith(prefix),names))

    