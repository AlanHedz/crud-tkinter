import sys
from pony.orm import *

sql_debug(True)

db = Database()

class Persona(db.Entity):
	name = Required(str)
	age = Required(int)

db.bind('postgres', user='postgres', password='lol123', host='localhost', database='python_demo')
db.generate_mapping(create_tables=True)