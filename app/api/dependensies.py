from fastapi import Depends
from services.impl.account_service import AccountService
from data.repositories.impl.account_repository import AccountRepository
from services.impl.user_service import UserService
from services.impl.suggestions_service import SuggestionsService
from data.repositories.impl.user_repository import UserRepository
from core.database import get_db

db = next(get_db())
_account_repository = AccountRepository(db)
_account_service = AccountService(_account_repository)
_user_repository = UserRepository(db)
_user_service = UserService(_user_repository,_account_service)

_suggestions_service = SuggestionsService(_user_repository)

def get_user_service():
    return _user_service

def get_suggestions_service():
    return _suggestions_service

def get_user_repository():
    return _user_repository