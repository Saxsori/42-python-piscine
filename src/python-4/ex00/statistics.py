
def ft_statistics(*args: any, **kwargs: any) -> None:
	"""Print the statistics of the given list"""

	stat_func = {
		'mean': lambda val: sum(val) / len(val),
		'median': lambda val: sorted(val)[len(val) // 2],
		'quartile': lambda val: [float(sorted(val)[len(val) // 4]), float(sorted(val)[len(val) // 4 * 3])],
		'var': lambda val: float(sum((x - stat_func['mean'](val)) ** 2 for x in val) / len(val)),
		'std': lambda val: float(stat_func['var'](val) ** 0.5)
	}
 
	try:
		assert len(args) > 0
		assert len(kwargs) > 0
		
		for stat in kwargs.values():
			if stat in stat_func.keys():
				print(f'{stat} : {stat_func[stat](list(args))}')
			else:
				assert False
	except AssertionError:
		print("ERROR")
	
