# app/api/dependensies.py
from fastapi import Depends
from services.impl.user_service import UserService
from services.impl.suggestions_service import SuggestionsService
from data.repositories.impl.InMemoryUserRepository import InMemoryUserRepository

# Создаем ОДИН экземпляр репозитория и сервиса
_user_repository = InMemoryUserRepository()
_user_service = UserService(_user_repository)
_suggestions_service = SuggestionsService(_user_repository)

def get_user_service():
    return _user_service  # ← возвращаем один и тот же экземпляр сервиса

def get_suggestions_service():
    return _suggestions_service