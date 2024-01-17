from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
	""""King is a great house of Westeros, ruling over the vast region known as the Stormlands from their seat at Storm's End."""
	
	def __init__(self, first_name, is_alive=True) -> None:
		"""Constructor for King"""
		super().__init__(first_name, is_alive)
	
	def set_eyes(self, color):
		"""Set the eyes color of the King"""
		self._eyes = color
	
	def set_hairs(self, color):
		"""Set the hairs color of the King"""
		self._hairs = color

	def get_eyes(self):
		"""Get the eyes color of the King"""
		return self._eyes

	def get_hairs(self):
		"""Get the hairs color of the King"""
		return self._hairs

	# properties are a special kind of attribute that have accessor methods associated with them.
	# property() is a built-in function that creates and returns a property object.
	# property() takes four arguments: fget, fset, fdel, and doc.
	# property() is typically used to create a managed attribute,
 	# i.e. an attribute that is protected by a getter and sette, that can not be set directly.
	eyes = property(get_eyes, set_eyes, doc="This is the eyes color of the King")
	hairs = property(get_hairs, set_hairs, doc="This is the hairs color of the King")
	
	
	
	
		