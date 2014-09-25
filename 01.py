def multiples(below, *args):
	multiples = []
	sum = 0
	for i in range(1, below):
		for j in range(len(args)):
			if i % args[j] == 0:
				if i not in multiples:
					multiples.append(i)
	for i in range(len(multiples)):
		sum += multiples[i]
	return sum