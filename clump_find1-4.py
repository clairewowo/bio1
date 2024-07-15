
# finds all distinct k-mers forming (L, t) clumps in a genome
# An (L, t) clump is a k-mer that occurs t or more times within a window of length L
def clump_find(filename):

	# helper function: returns a dictionary that shows frequencies of kmers
	def freq_table(text, k):
		d = {}
		for i in range(0, len(text) + 1):
			seq = text[i:i + k]
			if seq in d:
				d[seq] += 1;
			else:
				d[seq] = 1
		return d


	with open(filename) as reader:
		lines = reader.readlines()
		text = lines[0].strip()
		numbers = lines[1].strip().split()
		k = int(numbers[0])
		L = int(numbers[1])
		t = int(numbers[2])
		patterns = []

		for i in range(0, len(text) + 1):
			window = text[i: i + L]
			freqDict = freq_table(window, k)

			for key in freqDict.keys():
				if freqDict[key] >= t and key not in patterns:
					patterns += [key]

		for kmer in patterns:
			print(kmer + ' ')

clump_find('datasets/1-4dataset.txt')

