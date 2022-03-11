from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def match(self, text: str) -> bool:
        pass

    @abstractmethod
    def get_print(self) -> str:
        pass
