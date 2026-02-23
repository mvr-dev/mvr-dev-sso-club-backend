from fastapi import APIRouter, Depends
from data.models.update_request.user_update_request import UserUpdateRequest
from data.models import UserResponse
from services.iuser_service import IUserService
import api.dependensies as dependensies
from services.isuggestions_service import ISuggestionsService
from typing import List, Optional

router = APIRouter()

@router.get("/user",response_model=UserResponse)
async def getUser(id: int, userService: IUserService = Depends(dependensies.get_user_service)):
    # print(suggestionsService.getNames())
    return await userService.getUserById(id)

@router.put('/user',response_model=UserResponse)
async def updateUser(id: int, userUpdateRequest : UserUpdateRequest,userService: IUserService = Depends(dependensies.get_user_service)):
    return await userService.updateUser(id,userUpdateRequest)
