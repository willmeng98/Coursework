from hivSeqs import *
from distHelper import *
import math

def jukes(propDiff):
    """Correction for multiple hits using Jukes-Cantor model."""
    if propDiff < 0:
        print("jukes was passed a negative number, which it doesn't know how to handle.")
        return
    elif propDiff == 0:
        return 0
    elif propDiff < 0.75:
        return -3.0*math.log(1-(4.0*propDiff/3))/4
    else:
        print("jukes was passed a number >= 0.75, which is too big.")
        return

def propDifferent(seqA,seqB):
    total = 0
    diff = 0
    for i in range(0,len(seqA)):
        if((seqA[i] != '-') and (seqB[i] != '-')):
            total = total + 1
            if(seqA[i] == seqB[i]):
                diff = diff + 1
    return (total-diff)/total

def distances(strainNamesL,seqsL):
    dic = {}
    for i in range(0,len(strainNamesL)):
        for k in range(0,len(strainNamesL)):
            dic[(strainNamesL[i],strainNamesL[k])] = jukes(propDifferent(seqsL[i],seqsL[k]))
    return dic




"""print(propDifferent('A-T','CTT'))
print(propDifferent('GGG','TTG'))
print(propDifferent('CGA','C-A'))
D=distances(['a','b','c'],['ACTT','A-GT','TATT'])

print(sorted(D.items()))"""



