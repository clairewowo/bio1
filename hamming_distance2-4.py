
# finds the hamming distance, or the number of mismatches between the two strings
def distance(filename):
	with open(filename) as reader:
		lines = reader.readlines()
		str1 = lines[0].strip()
		str2 = lines[1].strip()
		distance = 0
		for i in range(0, len(str1)):
			if str1[i] != str2[i]:
				distance += 1
		return distance

print(distance('datasets/distance.txt'))

