import sys

def rollercoasterize(line):
	result = ""
	i = 0
	for char in list(line):
		if char.isalpha():
			i += 1
		if i % 2 == 0:
			result += char.lower()
		else:
			result += char.upper()
	return result

test_cases = open(sys.argv[1], 'r')
for line in test_cases:
	print rollercoasterize(line),

test_cases.close()
