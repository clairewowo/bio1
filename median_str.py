
nucl = ['A', 'T', 'C', 'G']
def distance(str1, str2):
	distance = 0
	for i in range(len(str2)):
		if str1[i] != str2[i]:
			distance += 1
	if len(str2) < len(str1):
		distance += len(str1) - len(str2)
	return distance

def neighbors(string, d):
	if d == 0:
		return [string]
	if len(string) == 1:
		return nucl # A, T, C, G
	neighbor = []
	first = string[0]
	suffix = string[1:]
	suffixes = neighbors(suffix, d)
	for text in suffixes:
		if distance(suffix, text) < d:
			for n in nucl:
				neighbor.append(n + text)
		else:
			neighbor.append(first + text)
	return neighbor

# generates all the possible kmers of length k
def generate_kmers(k):
	bases = ['A', 'T', 'C', 'G']
	last = bases
	current = []

	for i in range(k-1):
		for b in bases:
			for l in last:
				current.append(l + b)
		last = current
		current = []
	return last

    
# finds the minimum distance possible from all the frames in a string and a kmer
def find_min_distance(string, kmer):
	k = len(kmer)
	min_distance = k
	for i in range(len(string) -  k +1):
		window = string[i: i + k]
		d = distance(window, kmer)
		if d < min_distance:
			min_distance = d
	return min_distance

"""
Finds a median string that minimizes d(pattern, dna), where dna is a list of strings. 
If there are multiple kmers that minimize distance equally, only one of them needs to be returned. 
k is the length of the kmer to be found
k appears on the first line of the file, dna is on the second line, separated by spaces
"""

def median_string(filename):

	with open(filename) as reader:
		lines = reader.readlines()
		k = int(lines[0].strip())
		kmers = generate_kmers(k)

		dnas = lines[1].strip().split()

		min_distance = k * len(dnas)
		min_strand = ""
		for kmer in kmers:
			distance = 0
			for dna in dnas:
				distance += find_min_distance(dna, kmer)

			if distance <= min_distance:
				min_distance = distance
				min_strand = kmer
			
		return min_strand


print(median_string('datasets/median2.txt'))
#print(find_min_distance('AAATTGACGCAT', 'CCA'))




