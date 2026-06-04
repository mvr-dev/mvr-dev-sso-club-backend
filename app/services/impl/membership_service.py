from typing import List
from data.models.update_request.membership_update_request import MembershipUpdateRequest
from data.models.response.membership_repsonce import MembershipResponse
from data.models.membership import Membership

from data.repositories.imembership_repository import IMembershipRepository
from services.imembership_service import IMembershipService


class MembershipService(IMembershipService):
    def __init__(self, membershipRepository: IMembershipRepository):
        self._repository = membershipRepository

    async def getmembershipByID(self, id: int) -> MembershipResponse:
        membership = await self._repository.getmembershipByID(id)
        return MembershipResponse(
            membership_id=membership.membership_id,
            person_id=membership.person_id,
            community_id=membership.community_id,
            joined_at=membership.joined_at,
            status=membership.status,
            left_at=membership.left_at
        )
    
    async def getAllMembership(self) -> List[MembershipResponse]:
        memberships = await self._repository.getAllMembership()
        return [
            MembershipResponse(
                membership_id=m.membership_id,
                person_id=m.person_id,
                community_id=m.community_id,
                joined_at=m.joined_at,
                status=m.status,
                left_at=m.left_at
            ) for m in memberships
        ]
    
    async def addMembership(self, user_id: int, community_id: int) -> MembershipResponse:
        membership = Membership(
            person_id=user_id,
            community_id=community_id
        )
        created_membership = await self._repository.addMembership(membership)
        return MembershipResponse(
            membership_id=created_membership.membership_id,
            person_id=created_membership.person_id,
            community_id=created_membership.community_id,
            joined_at=created_membership.joined_at,
            status=created_membership.status,
            left_at=created_membership.left_at
        )
    
    async def updateMembership(self, update_request: MembershipUpdateRequest) -> MembershipResponse:
        # Создаем объект Membership из запроса на обновление
        membership = Membership(
            membership_id=update_request.membership_id,
            person_id=update_request.person_id,
            community_id=update_request.community_id,
            status=update_request.status,
            joined_at=update_request.joined_at,
            left_at=update_request.left_at
        )
        updated_membership = await self._repository.updateMembership(membership)
        return MembershipResponse(
            membership_id=updated_membership.membership_id,
            person_id=updated_membership.person_id,
            community_id=updated_membership.community_id,
            joined_at=updated_membership.joined_at,
            status=updated_membership.status,
            left_at=updated_membership.left_at
        )
    
    async def deleteMembership(self, id: int) -> MembershipResponse:
        deleted_membership = await self._repository.deleteMembership(id)
        return MembershipResponse(
            membership_id=deleted_membership.membership_id,
            person_id=deleted_membership.person_id,
            community_id=deleted_membership.community_id,
            joined_at=deleted_membership.joined_at,
            status=deleted_membership.status,
            left_at=deleted_membership.left_at
        )