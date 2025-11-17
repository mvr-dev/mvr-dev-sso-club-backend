from abc import ABC, abstractmethod
from typing import List


class ISuggestionsService(ABC):

    @abstractmethod
    def getNames(self,prefix:str)->List[str]:
        pass

    @abstractmethod
    def getSurnames(self,prefix:str)->List[str]:
        pass

    @abstractmethod
    def addName(self,name:str)->None:
        pass

    @abstractmethod
    def addSurname(self,surname:str)->None:
        pass