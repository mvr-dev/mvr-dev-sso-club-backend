from fastapi import APIRouter, Depends
from data.models import UserResponse, UserCreateRequest
from services.iuser_service import IUserService
import api.dependensies as dependensies
from services.isuggestions_service import ISuggestionsService
from typing import List, Optional

router = APIRouter()

@router.get("/me",response_model=UserResponse)
async def getNames(id: int, userService: IUserService = Depends(dependensies.get_user_service)):
    # print(suggestionsService.getNames())
    return await userService.getUserById(id)

