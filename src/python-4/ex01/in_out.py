
def square(x: int | float) -> int | float:
	""" Return the square of a number """
	return x * x

def pow(x: int | float) -> int | float:
	""" Return the power of a number """
	return x ** x

def outer(x: int | float, function) -> object:
	count = x
	def inner() -> float:
		nonlocal count
		count = function(count)
		return count
	return inner