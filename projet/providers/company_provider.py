from models import Company
from typing import List
from models import Entity
from providers import EntityProvider
import sqlite3

class CompanyProvider(EntityProvider):
    def search(self, text: str) -> List[Entity]:
        con = sqlite3.connect('inventory.db')
        cur = con.cursor()
        search_text: str = '%' + text + '%'
        results = []
        for row in cur.execute("SELECT name FROM company WHERE name LIKE ?", (search_text, )):
            name: str = row[0]
            company: Company = Company(name)
            results.append(company)
        return results
