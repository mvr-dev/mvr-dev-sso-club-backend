from enum import Enum


class MembershipType(Enum):
    ACTIVE = 'active'
    PAUSED = 'paused'
    LEFT = 'left'