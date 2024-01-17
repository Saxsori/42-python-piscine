from abc import ABC, abstractmethod

# ABC = Abstract Base Class is a class that is meant to be inherited from, but not instantiated.
# ABCs are used to enforce a certain programming paradigm or an API.
# ABCs are not required for interfaces, but they can be used to define one.
# ABCs are not required for abstract classes, but they can be used to define one.

class Character(ABC):
	"""Your docstring for Class"""
	@abstractmethod
	def die(self):
		"""Your docstring for Method"""
		pass
	
	def __init__(self, first_name, is_alive=True) -> None:
		"""Your docstring for Method"""
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(Character):
	"""Your docstring for Class"""
	def __init__(self, first_name, is_alive=True) -> None:
		"""Your docstring for Method"""
		super().__init__(first_name, is_alive)
	
	def die(self):
		"""Your docstring for Method"""
		self.is_alive = False
  
