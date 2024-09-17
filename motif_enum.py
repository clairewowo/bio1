

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

# finds if a kmer exists in a dna strand with at most d mismatches
def exists(dna, kmer, d):
	k = len(kmer)
	for i in range(len(dna) - len(kmer) + 1):
		window = dna[i: i+ k]
		if distance(window, kmer) <= d:
			return True
	return False

# finds all (k, d)-motifs in Dna
def motif_enumeration(filename):
	with open(filename) as reader:
		lines = reader.readlines()
		k = int(lines[0][0])
		d = int(lines[0][2])
		motifs = []
		dnas = lines[1].strip().split()

		for dna in dnas:
			for i in range(len(dna) - k + 1):
				kmer = dna[i: i + k]
				neighbor = neighbors(kmer, d)

				# goes through other dna strands to see if kmer with d mismatches exists
				for n in neighbor:
					count = 0
					for j in range(len(dnas)):
						strand = dnas[j]
						if strand != dna and exists(strand, n, d):
							count += 1
					if (count == len(dnas) - 1) and n not in motifs:
						motifs.append(n)
		return motifs


motifs = motif_enumeration('datasets/motif2.txt')
output = ""
for m in motifs:
	output += m + ' '

print(output)






