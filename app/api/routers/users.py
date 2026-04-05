from fastapi import APIRouter, Depends
from data.models import UserResponse, UserCreateRequest
from services.iuser_service import IUserService
import api.dependensies as dependensies
from services.isuggestions_service import ISuggestionsService
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List, Optional
from services.auth.utils import decode

router = APIRouter()
http_bearer = HTTPBearer()

async def get_current_auth_user(
        token : HTTPAuthorizationCredentials = Depends(http_bearer),
        userService: IUserService = Depends(dependensies.get_user_service)
    ):
    payload = decode(token=token.credentials)
    print(payload)
    return await userService.getUserById(int(payload["sub"]))
    

@router.get("/user",response_model=UserResponse)
async def getNames(user = Depends(get_current_auth_user)):
    # print(suggestionsService.getNames())
    return  user

