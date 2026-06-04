


from datetime import datetime

from pydantic import BaseModel

from data.models.enums.membership_type_enum import MembershipType


class Membership(BaseModel):
    

    membership_id :int
    person_id : int
    community_id :int
    joined_at : datetime
    status : MembershipType
    left_at : datetime
