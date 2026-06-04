from enum import Enum


class CommunityStatus(Enum):
    DRAFT = "DRAFT"
    ACTIVE = 'ACTIVE'
    PAUSED = 'PAUSED'
    CLOSED = 'CLOSED'
    ARCHIVED = 'ARCHIVED'