from services import LcsService

class AppController:
    def __init__(self, service: LcsService) -> None:
        self.__service = service

    def compute(self, text1: str, text2: str) -> int:
        return self.__service.extract_longest_common_sequence(text1, text2)