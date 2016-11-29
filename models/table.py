import sys
from pony.orm import *

sql_debug(True)

db = Database()

class Persona(db.Entity):
	name = Required(str)
	age = Required(int)

db.bind('', user='', password='', host='', database='')
db.generate_mapping(create_tables=True)