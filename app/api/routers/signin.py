from fastapi import APIRouter, Depends
from data.models import UserResponse, UserCreateRequest
from services.impl.UserService import UserService
import api.dependensies as dependensies
from services.isuggestions_service import ISuggestionsService
from typing import List, Optional

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(
    userCreateRequest: UserCreateRequest, 
    userService: UserService = Depends(dependensies.get_user_service)
):
    return await userService.addUser(userCreateRequest)

@router.post("/signin")
async def signin():
    return {"message": "Signin endpoint works!"}

@router.get("/names",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)):
    return await suggestionsService.getNames(prefix)

@router.get("/surnames",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)):
    return await suggestionsService.getSurnames(prefix)