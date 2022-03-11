from typing import List
from models import Entity
from providers import EntityProvider

class SearchService:
    def __init__(self, providers: List[EntityProvider]) -> None:
        self.__providers = providers

    def search(self, text: str) -> List[Entity]:
        results = []
        for provider in self.__providers:
            provider_results = provider.search(text)
            results = results + provider_results
        return results