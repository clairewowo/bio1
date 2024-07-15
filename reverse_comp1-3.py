
# finds the reverse compliment of the DNA strand
def reverse_compliment(file):
	with open(file) as reader:
		text = reader.readline().strip()
		output = ""
		comps = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

		for char in text:
			output += comps[char]
		print(output[::-1])

reverse_compliment('datasets/sequence1.txt')