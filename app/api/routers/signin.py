from fastapi import APIRouter, Depends
from data.models.token import TokenInfo
from data.models.user import User
from data.models import UserResponse, UserCreateRequest
from services.iuser_service import IUserService
import api.dependensies as dependensies
from services.isuggestions_service import ISuggestionsService
from typing import List, Optional
import services.auth.utils as jwt_utils

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(
    userCreateRequest: UserCreateRequest, 
    userService: IUserService = Depends(dependensies.get_user_service),
    suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)
):
    await suggestionsService.addName(userCreateRequest.name)
    await suggestionsService.addSurname(userCreateRequest.surname)
    return await userService.addUser(userCreateRequest)

@router.post("/login",response_model=TokenInfo)
async def auth_issue_jwt(user: User = Depends(dependensies.get_user_service().validate_user)):
    user = await user
    jwt_payload = {
        'sub':user.id,
        'name' : user.surname+" "+user.name,
        'email' : user.email
    }
    token = jwt_utils.encode(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="bearer"
    )

@router.get("/names",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)):
    # print(suggestionsService.getNames())
    return await suggestionsService.getNames(prefix)

@router.get("/surnames",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_suggestions_service)):
    return await suggestionsService.getSurnames(prefix)