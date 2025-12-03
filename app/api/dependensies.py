from fastapi import Depends
from services.impl.user_service import UserService
from services.impl.suggestions_service import SuggestionsService
from data.repositories.impl.user_repository import UserRepository
from core.database import get_db

db = next(get_db())
_user_repository = UserRepository(db)
_user_service = UserService(_user_repository)
_suggestions_service = SuggestionsService(_user_repository)

def get_user_service():
    return _user_service

def get_suggestions_service():
    return _suggestions_service

def get_user_repository():
    return _user_repository