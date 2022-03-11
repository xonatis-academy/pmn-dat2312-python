from typing import List
from services import SearchService

class AppController:
    def __init__(self, search_service: SearchService) -> None:
        self.__service = search_service

    def search(self, text: str) -> List[str]:
        results = self.__service.search(text)
        return [e.get_print() for e in results]