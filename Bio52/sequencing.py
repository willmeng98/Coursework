import copy
import doctest


def lcsHelper(s1, s2, length = 0, c1 = None, c2 = None):
    
    'helper function for the lcs function. takes in the length and saves the copies'

    #copy string
    if c1 == None:
        c1 = ''
    if c2 == None:
        c2 = ''
    #base case
    if not s1 or not s2:
        return (length, c1, c2)

    if s1[0] == s2[0]:
        useIt = lcsHelper(s1[1:], s2[1:], length +1, c1 + s1[0], c2 + s2[0])
    else:
        useIt = (0, '', '')

    loseIt2 = lcsHelper(s1[1:], s2, length, c1 + '#', c2)
    loseIt1 = lcsHelper(s1, s2[1:], length, c1, c2 + '#')

    return max(useIt, loseIt1, loseIt2)

def lcs(s1, s2):
    'new lcs function that find the lcs and replaces the rest with #'
    '''
    >>> lcs("x", "y")
    (0, '#', '#')               <-- the LCS has length 0. It uses neither "x" nor "y"
    >>> lcs("spam", "")
    (0, '####', '')             <-- the LCS has length 0. None of the letters in either string are used
    >>> lcs("spa", "m")
    (0, "###", "#")             <-- nothing is used in either string, so we stamp everything out!
    >>> lcs("cat", "car")
    (2, "ca#, "ca#")            <-- the "ca" is common but the "t" and "r" don't match
    >>> lcs("cat", "lca")
    (2, "ca#", "#ca")           <-- the "ca" is still the longest common part
    >>> lcs("human", "chimpanzee")
    (4, 'h#man', '#h#m#an###')

    '''
    answer = lcsHelper(s1, s2)
    #print(answer)
    extraS1Hash = ['#' for i in range(len(s1) - len(answer[1]))]
    extraS2hash = ['#' for i in range(len(s2) - len(answer[2]))]
    return (answer[0], answer[1]+ ''.join(extraS1Hash), answer[2] + ''.join(extraS2hash))

def alHelper(s1, s2, length = 0, copys1 = None, copys2 = None):

    'helper for align by taking in copys'

    #copies
    if copys1 == None:
        copys1 = '' 
    if copys2 == None:
        copys2 = ''
    #base case: length of either string is 0
    if not s1 or not s2:
        return (length, copys1+s2, "".join(['-' for i in range(len(s1))])) if not s2 else (length,"".join(['-' for i in range(len(s2))]) ,copys2+s2)
    if s1==s2:
        return (length + len(s1), copys1+s1, copys2+s2)
    if len(s1)==1 and len(s2)==1 and s1 != s2:
        return (length, copys1 +s1 + '-', copys2 + '-' + s2)

    if s1[0] == s2[0]:
        useIt = alHelper(s1[1:], s2[1:], length +1, copys1 + s1[0], copys2 + s2[0])
    else:
        useIt = (0, s1[0], s2[0])

    loseIt2 = alHelper(s1[1:], s2, length, copys1 + s1[0],  copys2 +'-')
    loseIt1 = alHelper(s1, s2[1:], length, copys1 + '-', copys2 +s2[0])
    #print(loseIt2)
    #print(loseIt1)
    return max(useIt, loseIt1, loseIt2)

def align(s1, s2):
    'Find lcs but the result will contain a hyphen symbol at any location where they mismatch.'
    '''
    >>> align("x", "y")
    (0, 'x-', '-y')         <-- The solution (0, '-x', 'y-') is also fine
    >>> align("spam", "")   <-- Take a close look here; this is a base case...
    (0, 'spam', '----')     <-- ... notice that the second string is all ---- 
                            so that it has the same length as the first
    >>> align("cat", "car")
    (2, 'cat-', 'ca-r')     
    >>> align("hi", "ship")
    (2, '-hi-', 'ship')
    >>> align("ATTGC", "GATC")
    (3, '-ATTGC', 'GAT--C')
    '''
    answer = alHelper(s1, s2)
    extraS1Hash = ['-' for i in range(len(s1) - len(answer[1]))]
    extraS2hash = ['-' for i in range(len(s2) - len(answer[2]))]
    return (answer[0], answer[1]+ ''.join(extraS1Hash), answer[2] + ''.join(extraS2hash))

print(lcs("human","chimpanzee"))
print(align("ATTGC", "GATC"))


#print(doctest.testmod())