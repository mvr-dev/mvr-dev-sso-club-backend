
from abc import ABC, abstractmethod

from data.models.user import Credentials


class IAuthService(ABC):
    
    @abstractmethod
    def validate_user(self,creds : Credentials):
        pass
