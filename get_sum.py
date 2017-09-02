def get_sum(one, two, delimeter=' '):
	one = str(one)
	one = one.upper()
	two = str(two)
	two = two.upper()
	return str(one) + str(delimeter) + str(two)
print(get_sum('Hello', 2))