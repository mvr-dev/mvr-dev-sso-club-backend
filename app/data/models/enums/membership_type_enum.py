from enum import Enum


class MembershipType(Enum):
    ACTIVE = 'ACTIVE'
    PAUSED = 'PAUSED'
    LEFT = 'LEFT'