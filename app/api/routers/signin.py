# from fastapi import APIRouter
# from data import UserResponse, UserCreateRequest

# router = APIRouter()

# @router.post("/register", response_model=UserResponse)
# async def register(user_data: UserCreateRequest):
#     return UserResponse(
#         id=1,
#         name=user_data.name,
#         surname=user_data.surname
#     )

# @router.post("/signin")
# async def signin():
#     return {"message": "Signin endpoint works!"}

# app/api/routers/signin.py
from fastapi import APIRouter, Depends
from data import UserResponse, UserCreateRequest
from services.UserService import UserService
import api.dependensies as dependensies

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(
    userCreateRequest: UserCreateRequest, 
    userService: UserService = Depends(dependensies.get_user_service)  # ← БЕЗ СКОБОК!
):
    return await userService.addUser(userCreateRequest)

@router.post("/signin")
async def signin():
    return {"message": "Signin endpoint works!"}