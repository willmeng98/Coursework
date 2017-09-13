import doctest

def lcsHelper(s1, s2, length = 0, copys1 = None, copys2 = None):
	'''
	Returns tuple indicating length of lcsHelper and copy of s1 and s2 with # marked for unused chars
	>>> lcsHelper("human", "chimpanzee")
	(4, 'h#man', '#h#m#an###')
	'''
	# initialize copies
	if copys1 == None:
		copys1 = ''
	if copys2 == None:
		copys2 = ''
	# base case: length of either string is 0
	if not s1 or not s2:
		return (length, copys1, copys2)

	if s1[0] == s2[0]:
		useIt = lcsHelper(s1[1:], s2[1:], length +1, copys1 + s1[0], copys2 + s2[0])
	else:
		useIt = (0, '', '')

	loseIt2 = lcsHelper(s1[1:], s2, length, copys1 + '#', copys2)
	loseIt1 = lcsHelper(s1, s2[1:], length, copys1, copys2 + '#')

	return max(useIt, loseIt1, loseIt2)

def lcs(s1, s2):
	answer = lcsHelper(s1, s2)
	print(answer)
	extraS1Hash = ['#' for i in range(len(s1) - len(answer[1]))]
	extraS2hash = ['#' for i in range(len(s2) - len(answer[2]))]
	return (answer[0], answer[1]+ ''.join(extraS1Hash), answer[2] + ''.join(extraS2hash))

print(lcs('cat', 'car'))
print(lcs('human', 'chimpanzee'))
print(lcs('ATTGC', 'GATC'))

