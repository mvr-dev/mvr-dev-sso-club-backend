from datetime import datetime

from pydantic import BaseModel

from data.models.enums.community_status_enum import CommunityStatus
from data.models.enums.community_type_enum import CommunityType


class Community(BaseModel):
    community_id : int 
    community_type : CommunityType
    name : str  
    purpose : str 
    status :   CommunityStatus 
    created_at : datetime
    updated_at : datetime