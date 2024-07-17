
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

#print(distance('datasets/distance.txt'))

def distance(kmer, text):
	distance = 0
	for i in range(0, len(kmer)):
		if kmer[i] != text[i]:
			distance += 1
	return distance

"""
finds the indexes of approximate matches of a kmer. 
kmer is the first line of the file, second line is the text, 
third line is the max hamming distance"""
def num_matches(filename):
	with open(filename) as reader:
		lines = reader.readlines()
		kmer = lines[0].strip()
		k = len(kmer)
		text = lines[1].strip()
		maximum = int(lines[2].strip())
		count = 0

		for i in range(0, len(text) - k + 1):
			frame = text[i: i+k]
			d = distance(kmer, frame)
			if d <= maximum:
				count += 1

		return count

print(num_matches('datasets/count.txt'))

