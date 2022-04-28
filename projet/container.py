from dependency_injector import containers, providers
from controllers.app_controller import AppController

from providers.company_provider import CompanyProvider
from providers.person_provider import PersonProvider
from services.search_service import SearchService

class Container(containers.DeclarativeContainer):

    bertrand = providers.Singleton(CompanyProvider)
    archibald = providers.Singleton(PersonProvider)
    thomas = providers.Singleton(SearchService, providers=[bertrand(), archibald()])
    anna = providers.Singleton(AppController, search_service=thomas())

