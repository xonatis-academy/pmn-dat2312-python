from dependency_injector import containers, providers
from controllers.app_controller import AppController

from providers.company_provider import CompanyProvider
from providers.person_provider import PersonProvider
from services.search_service import SearchService

class Container(containers.DeclarativeContainer):

    company_provider = providers.Singleton(CompanyProvider)
    person_provider = providers.Singleton(PersonProvider)
    search_service = providers.Singleton(SearchService, providers=[company_provider(), person_provider()])
    controller = providers.Singleton(AppController, search_service=search_service())

