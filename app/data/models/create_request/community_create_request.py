from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from data.models.enums.community_status_enum import CommunityStatus
from data.models.enums.community_type_enum import CommunityType


class CommunityCreateRequest(BaseModel):  
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True  # разрешает принимать и snake_case, и camelCase
    )
      
    community_type : CommunityType
    name : str  
    purpose : str 