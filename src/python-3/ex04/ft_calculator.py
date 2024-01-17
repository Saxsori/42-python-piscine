class calculator:
	
	""" Calculator class to perform Vector operations """
 
	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		""" Vector dot product """
		result = sum([V1[i] * V2[i] for i in range(len(V1))])
		print("The dot product is : ", result)

		
	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		""" Vector addition """
		result = [float(V1[i] + V2[i] )for i in range(len(V1))]
		print("The addition of the vectors is : ", result)
	
	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		""" Vector subtraction """
		result = [float(V1[i] - V2[i]) for i in range(len(V1))]
		print("The subtraction of the vectors is : ", result)