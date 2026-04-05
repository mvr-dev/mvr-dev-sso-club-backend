from fastapi import APIRouter, Depends
from data.models.token import TokenInfo
from data.models.user import User
from data.models import UserResponse, UserCreateRequest
from services.iuser_service import IUserService
import api.dependensies as dependensies
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
        'sub': str(user.id),
        'name' : user.surname+" "+user.name,
        'email' : user.email
    }
    token = jwt_utils.encode(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="bearer"
    )
