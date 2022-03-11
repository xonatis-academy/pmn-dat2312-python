class Coeur:
    def __init__(self):
        self.couleur = 'Rouge'

class Person:
    def __init__(self) -> None:
        self.__coeur = None

c1 = Coeur()
michael = Person()
michael.__coeur = c1 # Bad as __coeur is private

c2 = Coeur()
hugo = Person()
hugo.__coeur = c2 # Bad as __coeur is private