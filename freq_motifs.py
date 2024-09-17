
# A function that finds the most frequent k-mers (sequences of letters k letters long) within 
# the text in the file. Returns the most frequent k-mers, separated by spaces if there are multiple. 
def freq_words(file_name):
	with open(file_name) as reader:
		lines = reader.readlines()
		data = lines[0]
		k = int(lines[1])
		kmers_dict = {}
		for i in range(0, len(data) - k + 1):
			kmer = data[i:i + k]
			if kmer in kmers_dict:
				kmers_dict[kmer] += 1
			else:
				kmers_dict[kmer] = 1

		most_frequent = []
		maximum = -1

		for (key,val) in kmers_dict.items():
			if val >= maximum:
				if val > maximum:
					most_frequent = []
				maximum = val
				most_frequent += [key]

		output = ""
		for word in most_frequent:
			output += word + ' '
		print(output)

freq_words('datasets/quiz1.txt')