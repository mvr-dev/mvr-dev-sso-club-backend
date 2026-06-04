from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException,status

from api import dependensies
from api.routers.users import get_current_auth_user
from data.models.user import User
from services.imembership_service import IMembershipService
from data.models.response.community_responce import CommunityResponce
from services.icommunity_service import ICommunityService
from data.models.create_request.community_create_request import CommunityCreateRequest
from data.models.enums.community_status_enum import CommunityStatus
from data.models.enums.community_type_enum import CommunityType
from data.models.community import Community



router = APIRouter()

@router.get("/membership/{community_id}")
async def join_community(community_id,membershipService : IMembershipService = Depends(dependensies.get_membership_service),user : User = Depends(get_current_auth_user)):
    membershipService.addMembership(user.id,community_id)

@router.delete('/membership/{community_id}')
async def leave_community(community_id,membershipService : IMembershipService = Depends(dependensies.get_membership_service),user : User = Depends(get_current_auth_user)):
    user.name
    pass

@router.get("/membership")
async def get_memberships(membershipService : IMembershipService = Depends(dependensies.get_membership_service),user : User = Depends(get_current_auth_user)):
    user.name
    pass

@router.put('/membership/{community_id}')
async def update_membership(membershipService : IMembershipService = Depends(dependensies.get_membership_service),user : User = Depends(get_current_auth_user)):
    user.name
    pass