
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

l = neighbors('ACG', 1)
output = ""

for n in l:
	output += n + ' '
print(output)
