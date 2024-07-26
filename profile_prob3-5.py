

"""
Profile-most probable kmer problem
Input: dna (text), integer k, and a 4 * k profile matrix
Ouput: the most probable kmer in text
"""
def profile_prob(filename):
	with open(filename) as reader:
		lines = reader.readlines()
		dna = lines[0].strip()
		k = int(lines[1].strip())
		matrix = []

		for i in range(2, len(lines)):
			matrix.append(lines[i].strip().split()) # add each line to the matrix

		

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				matrix[i][j] = float(matrix[i][j])

		# print(matrix)

		indexes = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
		kmers = {}

		for i in range(len(dna) - k + 1):
			window = dna[i: i+k]
			product = 1
			for j in range(len(window)):
				row = indexes[window[j]]
				product *= matrix[row][j]

			if window not in kmers:
				kmers[window] = product

		max_score = 0
		max_kmer = ""
		for key in kmers:
			if kmers[key] > max_score:
				max_score = kmers[key]
				max_kmer = key
				
		return max_kmer

print(profile_prob('datasets/profile.txt'))



