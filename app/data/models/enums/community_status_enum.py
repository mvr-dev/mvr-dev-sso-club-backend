from enum import Enum


class CommunityStatus(Enum):
    DRAFT = "draft"
    ACTIVE = 'active'
    PAUSED = 'paused'
    CLOSED = 'closed'
    ARCHIVED = 'archived'