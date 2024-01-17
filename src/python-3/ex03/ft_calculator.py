class calculator:
	""" Calculator class to perform basic operations """
	def __init__(self, numbers) -> None:
		self.numbers = numbers

	def __add__(self, object) -> None:
		""" Vector addition """
		self.numbers = [item + object for item in self.numbers]
		print(self.numbers)

	def __mul__(self, object) -> None:
		""" Vector multiplication """
		self.numbers = [item * object for item in self.numbers]
		print(self.numbers)
  
	def __sub__(self, object) -> None:
		""" Vector subtraction """
		self.numbers = [item - object for item in self.numbers]
		print(self.numbers)
  
	def __truediv__(self, object) -> None:
		""" Vector division """
		try:
			self.numbers = [item / object for item in self.numbers]
			print(self.numbers)
		except ZeroDivisionError:
			print("division by zero is not possible")

