from models import Person
from providers import EntityProvider

class PersonProvider(EntityProvider):
    def __init__(self) -> None:
        self._data = [
            Person('Annie', 'Versaire'), 
            Person('Jean', 'Aimarre'),
            Person('Vincent', 'Time')
        ]
