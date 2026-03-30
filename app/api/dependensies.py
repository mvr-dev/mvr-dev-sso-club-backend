from fastapi import Depends
from services.impl.account_service import AccountService
from data.repositories.impl.account_repository import AccountRepository
from services.impl.user_service import UserService
from services.impl.names_suggestions_service import NamesSuggestionsService
from services.impl.surnames_suggestion_service import SurnamesSuggestionsService
from services.impl.city_suggestion_service import CitiesSuggestionsService
from services.impl.streets_suggestions_service import StreetsSuggestionsService
from data.repositories.impl.user_repository import UserRepository
from core.database import get_db

db = next(get_db())
_account_repository = AccountRepository(db)
_account_service = AccountService(_account_repository)
_user_repository = UserRepository(db)
_user_service = UserService(_user_repository,_account_service)

_names_suggestions_service = NamesSuggestionsService(_user_repository)
_surnames_suggestion_service = SurnamesSuggestionsService(_user_repository)
_cities_suggestion_service = CitiesSuggestionsService(_user_repository)
_streets_suggestion_service = CitiesSuggestionsService(_user_repository)



def get_user_service()->UserService:
    return _user_service

def get_names_suggestions_service() -> NamesSuggestionsService:
    return _names_suggestions_service
def get_surnames_suggestion_service() -> SurnamesSuggestionsService:
    return _surnames_suggestion_service
def get_cities_suggestion_service() -> CitiesSuggestionsService:
    return _cities_suggestion_service
def get_streets_suggestion_service() -> StreetsSuggestionsService:
    return _streets_suggestion_service

def get_user_repository() -> UserRepository:
    return _user_repository

def get_account_service() ->AccountService:
    return _account_service