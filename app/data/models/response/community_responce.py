from typing import Optional

from pydantic import BaseModel

from data.models.enums.community_status_enum import CommunityStatus
from data.models.enums.community_type_enum import CommunityType


class CommunityResponce(BaseModel):
    community_id : Optional[int] 
    community_type : CommunityType
    name : str  
    purpose : str 
    status :   CommunityStatus 