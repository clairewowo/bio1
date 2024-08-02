
import numpy as np
indexes = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

# kmers is a list of kmers. Construct a profile matrix using pseudocounts
def construct_profile_matrix(kmers):
	t = len(kmers)
	k = len(kmers[0])

	# make a count matrix, first add 1 to each
	count_matrix = np.zeros((4, k)) + 1

	# go down each "column"
	for i in range(k):
		for kmer in kmers:
			letter = kmer[i]	
			count_matrix[indexes[letter]][i] += 1

	profile_matrix = count_matrix / (len(kmers) + 4)
	return profile_matrix


# finds the most likely kmer given a profile matrix and the sequence
def most_likely_kmer(matrix, kmer, k):
	kmers = {}

	for i in range(len(kmer) - k +1):
		window = kmer[i: i + k]
		product = 1
		for j in range(len(window)):
			row = indexes[window[j]]
			product *= matrix[row][j]
	
		if window not in kmers:
			kmers[window] = product

	max_score = 0
	max_kmer = ""

	for key in kmers.keys():
		if kmers[key] > max_score:
			max_score = kmers[key]
			max_kmer = key
			
	return max_kmer

"""calculates the score of updated motifs in a matrix by summing 
up how many mismatches there are per column. Higher score means less accurate. """
def score(motifs):

	# first find a median string
	median = ""

	for col in range(len(motifs[0])):
		column = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
		for row in range(len(motifs)): 
			letter = motifs[row][col]
			column[letter] += 1

		max_score = 0
		final_letter = ""
		for letter in column:
			if column[letter] > max_score:
				final_letter = letter 
				max_score = column[letter]

		median += final_letter

	# then calculate the score of the motif
	total = 0
	for motif in motifs:
		for col in range(len(motifs[0])):
			if motif[col] != median[col]:
				total += 1

	return total



def greedy_motif_search(filename):
	with open(filename) as reader:
		lines = reader.readlines()
		numbers = lines[0].strip().split()
		k = int(numbers[0])
		t = int(numbers[1])
		print(t)

		dnas = lines[1].strip().split()

		best_motifs = [seq[0:k] for seq in dnas]
		best_score = k * t

		for i in range(len(dnas[0]) - k + 1):
			motifs = [dnas[0][i:i+k]]
			for j in range(1, t):
				profile = construct_profile_matrix(motifs)
				most_probable = most_likely_kmer(profile, dnas[j], k)
				motifs.append(most_probable)
			if score(motifs) < best_score:
				best_motifs = motifs
				best_score = score(motifs)
		return best_motifs


motifs = greedy_motif_search('datasets/motifsagain.txt')
output = ""
for motif in motifs:
	output += motif + ' '

print(output)

"""
matrix = construct_profile_matrix(['GCA', 'TCA', 'CGC', 'CAC', 'TCG'])
print(matrix)
print(most_likely_kmer(matrix, 'GGCGTTCAGGCA', 3))"""

