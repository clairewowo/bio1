

# gives the indexes of a pattern's occurences in a certain sequence
def find_indexes(filename):
	with open (filename) as reader:
		lines = reader.readlines()
		pattern = lines[0].strip()
		sequence = lines[1].strip()
		occurences = []

		for i in range(0, len(sequence) + 1):
			substr = sequence[i : i + len(pattern)]
			if substr == pattern:
				occurences += [i]

		indexes = ""
		for num in occurences:
			indexes += str(num) + ' '
		print(indexes)


find_indexes('datasets/Vibrio_cholerae.txt')

