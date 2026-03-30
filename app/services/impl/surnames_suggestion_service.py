from data.repositories.iuser_repository import IUserRepository
from ..isuggestions_service import ISuggestionsService


class SurnamesSuggestionsService(ISuggestionsService):

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository
        self._surnames = set(['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Соколов'])

    async def getSuggestion(self, prefix):
        surnames_in_repo = set(map(lambda x: x.surname, await self._userRepository.getAllUsers()))
        surnames = surnames_in_repo | self._surnames
        return set(filter(lambda x: x.startswith(prefix),surnames))