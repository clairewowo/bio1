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
	
	output = ""
	for n in neighbors:
		output += n + ' '
	return output

print(neighbors('ACG', 1))