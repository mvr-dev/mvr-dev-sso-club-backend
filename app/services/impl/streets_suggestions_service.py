from data.repositories.iuser_repository import IUserRepository
from ..isuggestions_service import ISuggestionsService


class StreetsSuggestionsService(ISuggestionsService):

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository

    async def getSuggestion(self, prefix):
        streets_in_repo = set(map(lambda x: x.street, await self._userRepository.getAllUsers()))
        return set(filter(lambda x: x.startswith(prefix),streets_in_repo))