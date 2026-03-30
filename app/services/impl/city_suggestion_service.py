from data.repositories.iuser_repository import IUserRepository
from ..isuggestions_service import ISuggestionsService


class CitiesSuggestionsService(ISuggestionsService):

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository
        

    async def getSuggestion(self, prefix):
        cities_in_repo = set(map(lambda x: x.city, await self._userRepository.getAllUsers()))
        return set(filter(lambda x: x.startswith(prefix),cities_in_repo))