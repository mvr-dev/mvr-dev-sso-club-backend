from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException,status

from api import dependensies
from api.routers.users import get_current_auth_user
from data.models.response.community_responce import CommunityResponce
from services.icommunity_service import ICommunityService
from data.models.create_request.community_create_request import CommunityCreateRequest
from data.models.enums.community_status_enum import CommunityStatus
from data.models.enums.community_type_enum import CommunityType
from data.models.community import Community


router = APIRouter()

@router.get("/community/{id}", response_model=CommunityResponce)
async def getCommunity(id:int,communityService : ICommunityService = Depends(dependensies.get_community_service),
                       user = Depends(get_current_auth_user)):
    try:
        user.name
        return await communityService.getCommuntyByID(id=id)
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    

@router.post('/community',response_model=CommunityResponce)
async def postCommunity(communityCreateRequest: CommunityCreateRequest, communityService: ICommunityService = Depends(dependensies.get_community_service)):
    return await communityService.addCommunity(communityCreateRequest)