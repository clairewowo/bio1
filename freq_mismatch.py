

nucl = ['A', 'C', 'T', 'G']
def distance(str1, str2):
	distance = 0
	for i in range(len(str2)):
		if str1[i] != str2[i]:
			distance += 1
	if len(str2) < len(str1):
		distance += len(str1) - len(str2)
	return distance

# returns a list of all the strings that have a distance of d or less from the original string
def neighbors(string, d):
	if d == 0:
		return string
	if len(string) == 1:
		return nucl # A, T, C, G
	neighbors = []
	suffix = string[1:]
	suffixes = neighbors(suffix, d)
	for text in suffixes:
		if distance(suffix, text) < d:
			for n in nucl:
				neighbors.append(n + text)
		else:
			neighbors.append(string[0] + text)
	return neighbors


# finds the most frequent kmer that occurs in the text with up to d mismatches
# k and d are provided on the second line of the file, separated by a space
def freq_mismatch(filename):
	with open(filename) as reader:
		lines = reader.readlines()
		text = lines[0]
		k = int(lines[1][0])
		d = int(lines[1][2])

		kmers = {}
		for i in range(0, len(text) - k + 1):
			seq = text[i : i+k]
			options = neighbors(seq, d)
			for kmer in options:
				if kmer in kmers:
					kmers[kmer] += 1
				else:
					kmers[kmer] = 1

		maximum = -1
		freq = []
		for kmer in kmers:
			if kmers[kmer] >= maximum:
				maximum = kmers[kmer]
				freq.append(kmer)

		output = ""
		for kmer in freq:
			output += kmer + ' '

		return output

print(freq_mismatch('datasets/mismatch2.txt'))



