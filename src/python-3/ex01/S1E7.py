from S1E9 import Character

# properties are a special kind of attribute that have accessor methods associated with them.
# @property decorator is used to customize getters and setters for class attributes.
# __repr__ is used to compute the “official” string representation of an object and is typically used for debugging.
# __str__ is used to compute the “informal” string representations of an object and is typically used for logging.
#  the __str__() string is intended for users and the __repr__() string is intended for developers.

class Baratheon(Character):
	"""Baratheon is a great house of Westeros, ruling over the vast region known as the Stormlands from their seat at Storm's End."""
	def __init__ (self, first_name, is_alive=True) -> None:
		""" Constructor for Baratheon family"""
		super().__init__(first_name, is_alive)
		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "dark"
	
	def die(self):
		"""This method is called when the Baratheon family dies"""
		self.is_alive = False
	
	@property
	def __repr__(self) -> str:
		return f"<Bound Method Baratheon.__repr__ of Vector : {self.family_name, self.eyes, self.hairs}>"

	@property
	def __str__(self) -> str:
		return f"<Bound Method Baratheon.__str__ of Vector : {self.family_name, self.eyes, self.hairs}>"
	

class Lannister(Character):
    
	"""Lannister is a great house of Westeros, one of the richest and most powerful families and oldest dynasties."""
	
	def __init__ (self, first_name, is_alive=True) -> None:
		"""Constructor for Lannister family"""
		super().__init__(first_name, is_alive)
		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"
	
	@classmethod
	def create_lannister(self, first_name, is_alive):
		"""This method is called when the Lannister family is created"""
		return Lannister(first_name, is_alive)

	def die(self):
		"""This method is called when the Lannister family dies"""
		self.is_alive = False
  
	@property
	def __repr__(self) -> str:
		return f"<Bound Method Lannister.__repr__ of Vector : {self.family_name, self.eyes, self.hairs}>"

	@property
	def __str__(self) -> str:
		return f"<Bound Method Lannister.__str__ of Vector : {self.family_name, self.eyes, self.hairs}>"
