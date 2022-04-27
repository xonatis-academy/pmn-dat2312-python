from abc import ABC

class Console(ABC):
    def __init__(self) -> None:
        self.__isOn = False
        self.led = ''

    def allumer(self) -> None:
        self.__isOn = True
        self.led = 'Verte'

    def eteindre(self) -> None:
        self.__isOn = False
        self.led = ''

class PlayStation(Console):
    def __init__(self) -> None:
        super().__init__()

    def lireBr(self) -> None:
        self.allumer()
        print('Lecture en cours ...')

class Xbox(Console):
    def __init__(self) -> None:
        super().__init__()


play = PlayStation()
play.lireBr()
print(play.led)

xbox = Xbox()
print(xbox.led)
