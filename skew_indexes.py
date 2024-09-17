

# gives the indexes where skew attains a minimum
# skew: number of G - number of C
def skew(filename):

	with open(filename) as reader:

		text = reader.readlines()[0].strip()
		decreasing = False
		skew = 0
		minimum = 0

		for i in range(0, len(text)):
			ch = text[i]
			if ch == 'G':
				skew += 1
			elif ch == 'C':
				skew -= 1
			if skew < minimum:
				minimum = skew

		skew = 0
		indexes = []

		for i in range(0, len(text)):
			ch = text[i]

			if ch == 'G':
				skew += 1
			elif ch == 'C':
				skew -= 1
			if skew == minimum:
				indexes.append(i + 1)

		output = ""		
		for num in indexes:
			output += str(num) + ' '

		print(output)

skew('datasets/skew-dataset.txt')




