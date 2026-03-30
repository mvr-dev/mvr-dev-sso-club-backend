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
    userService: IUserService = Depends(dependensies.get_user_service)
    ):
    
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
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_names_suggestions_service)):
    # print(suggestionsService.getNames())
    return await suggestionsService.getSuggestion(prefix)

@router.get("/surnames",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_surnames_suggestion_service)):
    return await suggestionsService.getSuggestion(prefix)

@router.get('/cities',response_model=List[str])
async def getCities(prefix:str = "", suggestionsService: ISuggestionsService = Depends(dependensies.get_cities_suggestion_service)):
    return await suggestionsService.getSuggestion(prefix)

@router.get('/streets',response_model=List[str])
async def getStreets(prefix:str = "", suggestionService:ISuggestionsService = Depends(dependensies.get_streets_suggestion_service)):
    return await suggestionService.getSuggestion(prefix)