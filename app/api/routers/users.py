from fastapi import APIRouter, Depends, HTTPException, status
from jwt import ExpiredSignatureError
from data.models.update_request.user_update_request import UserUpdateRequest
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
    try:
        payload = decode(token=token.credentials)
        print(payload)
        return await userService.getUserById(int(payload["sub"]))
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {payload['sub']} not found"
        )
    

@router.get("/user",response_model=UserResponse)
async def getUser(user = Depends(get_current_auth_user)):
    # print(suggestionsService.getNames())
    return user

@router.put('/user',response_model=UserResponse)
async def updateUser(userUpdateRequest: UserUpdateRequest,
                     user = Depends(get_current_auth_user), 
                     userService:IUserService = Depends(dependensies.get_user_service)):
    return await userService.updateUser(user.id,userUpdateRequest,user)

@router.delete('/user')
async def deleteUser(user = Depends(get_current_auth_user),userService:IUserService = Depends(dependensies.get_user_service)):
    await userService.deleteUser(user.id)
    
    


