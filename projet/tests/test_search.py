from typing import List
import unittest
from container import Container
from models.company import Company

class TestSearch(unittest.TestCase):

    def test_search_company_provider(self):
        container = Container()
        bertrand = container.bertrand()
        results: List[Company] = bertrand.search('Go')
        self.assertEqual(results[0].get_name(), 'Google')

