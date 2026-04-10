from abc import ABC, abstractmethod
from typing import List


class ISuggestionsService(ABC):

    @abstractmethod
    def getSuggestion(self,prefix:str)->List[str]:
        pass

