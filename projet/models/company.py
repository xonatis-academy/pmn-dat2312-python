from models import Entity

class Company(Entity):
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, value: str) -> None:
        self.__name = value

    def match(self, text: str) -> bool:
        return text in self.__name

    def get_print(self) -> str:
        return self.__name
