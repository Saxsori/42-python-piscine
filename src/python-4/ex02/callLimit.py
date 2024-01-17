def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		def limit_function(*args: any, **kwds: any):
			try:
				nonlocal count
				if count >= limit:
					raise Exception("call too many times")
				count += 1
				return function(*args, **kwds)
			except Exception as e:
				print(f'Error: {function} {e} ')
		return limit_function
	return callLimiter