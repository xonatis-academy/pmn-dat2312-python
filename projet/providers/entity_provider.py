from abc import ABC, abstractmethod
from typing import List
from models import Entity

class EntityProvider(ABC):
    @abstractmethod
    def search(self, text: str) -> List[Entity]:
        pass