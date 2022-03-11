from models import Company
from providers import EntityProvider

class CompanyProvider(EntityProvider):
    def __init__(self) -> None:
        self._data = [
            Company('Google'), 
            Company('Microsoft'),
            Company('Apple')
        ]
