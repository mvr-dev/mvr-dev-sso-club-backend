from fastapi import APIRouter, Depends, status
from data.models import UserResponse, UserCreateRequest
from services.iuser_service import IUserService
import api.dependensies as dependensies
from services.isuggestions_service import ISuggestionsService
from typing import List, Optional

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    userCreateRequest: UserCreateRequest, 
    userService: IUserService = Depends(dependensies.get_user_service),
    suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)
):
    await suggestionsService.addName(userCreateRequest.name)
    await suggestionsService.addSurname(userCreateRequest.surname)
    return await userService.addUser(userCreateRequest)

@router.post("/signin")
async def signin():
    return {"message": "Signin endpoint works!"}

@router.get("/names",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)):
    # print(suggestionsService.getNames())
    return await suggestionsService.getNames(prefix)

@router.get("/surnames",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)):
    return await suggestionsService.getSurnames(prefix)