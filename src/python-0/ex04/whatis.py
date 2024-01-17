import sys


if (len(sys.argv) > 2) :
	print("AssertionError: more than one argument is provided")
elif (len(sys.argv) == 2) :    
	try :
		value = int(sys.argv[1])
		if (value % 2 == 0) :
			print("I'm Even.")
		else :
			print("I'm Odd.")
	except Exception :
		print("AssertionError: argument is not an integer")
