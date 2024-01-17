from abc import ABC, abstractmethod

# ABC = Abstract Base Class is a class that is meant to be inherited from, but not instantiated.
# ABCs are used to enforce a certain programming paradigm or an API.
# ABCs are not required for interfaces, but they can be used to define one.
# ABCs are not required for abstract classes, but they can be used to define one.

class Character(ABC):
	"""Character is the base class for all characters in life"""
	
	@abstractmethod
	def die(self):
		"""This method is called when the character dies"""
		pass
	
	def __init__(self, first_name, is_alive=True) -> None:
		"""Constructor for Character class """
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(Character):
	"""Stark is a great house of Westeros, ruling over the vast region known as the North from their seat in Winterfell."""

	def __init__(self, first_name, is_alive=True) -> None:
		"""Constructor for Stark family """
		super().__init__(first_name, is_alive)
	
	def die(self):
		"""This method is called when the Stark family dies"""
		self.is_alive = False
  
