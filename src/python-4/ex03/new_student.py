import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
	"""Generate a random id"""
	return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
	"""A student is defined by his name, surname, login, id and active status"""
	name: str
	surname: str
	active: bool = True
	login: str = field(init=False)
	id: str = field(default_factory=generate_id, init=False)

	def __post_init__(self):
		""" This method is called after the object is initialized"""
		self.login = self.name[0]+self.surname
	
