from models import Entity

class Person(Entity):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.__firstname = firstname
        self.__lastname = lastname

    def get_firstname(self) -> str:
        return self.__firstname

    def set_fistname(self, value: str) -> None:
        self.__firstname = value

    def get_lastname(self) -> str:
        return self.__lastname

    def set_lastname(self, value: str) -> None:
        self.__lastname = value

    def get_fullname(self) -> str:
        return self.__firstname + ' ' + self.__lastname

    def match(self, text: str) -> bool:
        return text in self.get_fullname()

    def get_print(self) -> str:
        return self.get_fullname()

