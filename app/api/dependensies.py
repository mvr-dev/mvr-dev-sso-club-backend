# app/api/dependensies.py
from fastapi import Depends
from services.UserService import UserService
from data.repositories.impl.InMemoryUserRepository import InMemoryUserRepository

# Создаем ОДИН экземпляр репозитория и сервиса
_user_repository = InMemoryUserRepository()
_user_service = UserService(_user_repository)

def get_user_service():
    return _user_service  # ← возвращаем один и тот же экземпляр сервиса