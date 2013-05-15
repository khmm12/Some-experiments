import random

def get_int(msg, minimum, maximum, default):
	while True:
		try:
			input_line = input(msg)
			if (not input_line and default is not None):
				return default
			input_number = int(input_line)

			if (minimum is None and maximum is None):
				return input_number
			elif (minimum is not None and maximum is not None):
				if not minimum <= input_number <= maximum:
					print("must be", minimum, "<= x <=", maximum)
				else:
					return input_number
			else:
				if maximum is not None:
					if not input_number <= maximum:
						print("must be <=", maximum)
					else:
						return input_number
				else:
					if not minimum <= input_number:
						print("must be >=", minimum)
					else:
						return input_number

		except ValueError as err:
			print(err)
		except EOFError:
			pass


rows = get_int("rows: ", 1, None, None)
columns = get_int("columns: ", 1, None, None)
minimum = get_int("minimum (or Enter for 0): ", None, None, 0)
maximum = get_int("maximum (or Enter for %d): " % minimum, minimum, None, minimum)

print()


max_num_len = max((len(str(minimum)), len(str(maximum))))
for row in range(rows):
	line = " "
	for column in range(columns):
		i = random.randint(minimum, maximum)
		s = str(i)	
		line += ' ' * (max_num_len - len(s)) + s + ' ' * 2
	print(line)
