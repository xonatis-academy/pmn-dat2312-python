from models import Person
from providers import EntityProvider
from typing import List
from models import Entity
import sqlite3

# Text : "an"
# SELECT firstname, lastname FROM person WHERE firstname LIKE '%an%' OR lastname LIKE '%an%'

# search_text : '%an%'
# SELECT firstname, lastname FROM person WHERE firstname LIKE ? OR lastname LIKE ?


class PersonProvider(EntityProvider):
    def search(self, text: str) -> List[Entity]:
        con = sqlite3.connect('inventory.db')
        cur = con.cursor()
        search_text: str = '%' + text + '%'
        results = []
        for row in cur.execute("SELECT firstname, lastname FROM person WHERE firstname LIKE ? OR lastname LIKE ?", (search_text, search_text)):
            firstname: str = row[0]
            lastname: str = row[1]
            person = Person(firstname, lastname)
            results.append(person)
        return results