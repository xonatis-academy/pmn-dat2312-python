from abc import ABC
from typing import List
from models import Entity

class EntityProvider(ABC):
    def search(self, text: str) -> List[Entity]:
        return [e for e in self._data if e.match(text)]