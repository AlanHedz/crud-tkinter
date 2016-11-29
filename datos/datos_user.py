import sys
sys.path.append('./models')
from table import *

@db_session
def all_persons():
	persons = db.select("SELECT * FROM persona")[:]
	return persons

@db_session
def create_person(name, age):
	Persona(name = name, age = age)

@db_session
def update_person(id_persona, name, age):
	person = Persona[id_persona]
	person.set(name = name, age = age)

@db_session
def delete_person(id_persona):
	Persona[id_persona].delete()