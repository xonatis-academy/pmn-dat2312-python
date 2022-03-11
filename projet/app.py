from controllers.app_controller import AppController
from providers import CompanyProvider, PersonProvider
from services.search_service import SearchService

company_provider = CompanyProvider()
person_provider = PersonProvider()
service = SearchService([company_provider, person_provider])
controller = AppController(service)

text = input('What are you looking for? ')
results = controller.search(text)
print(results)