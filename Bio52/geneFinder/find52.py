import math
from findHelper import *

def find52():
    """Given coding and noncoding training data from E. coli, build a
    first order Markov model on codons and make predictions for
    sequences in Vibrio.
    """
    # load sequences
    ecoliCodeOrfL=[s.rstrip() for s in open("ecoliCodeTrainOrfs-mid.txt","r").readlines()]
    ecoliNoncodeOrfL=[s.rstrip() for s in open("ecoliNcTrainOrfs-mid.txt","r").readlines()]
    vibAllOrfL=[s.rstrip() for s in open("vibAllOrfs-mid.txt","r").readlines()]
    # run model
    ecoliCodeProbD=condProb(ecoliCodeOrfL)
    ecoliNoncodeProbD=condProb(ecoliNoncodeOrfL)
    llrD=makeLogLikelihoodRatioD(ecoliCodeProbD,ecoliNoncodeProbD)
    vibCodePredL,vibNoncodePredL=predict(vibAllOrfL,llrD)

    return vibCodePredL,vibNoncodePredL

def makeLogLikelihoodRatioD(codeProbD,noncodeProbD):
    """Make a dictionary of log likelihood ratios from coding and
    noncoding Markov models."""
    llrD={}
    for key in codeProbD:
        llrD[key] = math.log( codeProbD[key]/noncodeProbD[key] )
    return llrD

def count(orfL):
    codonCountD,twoCodonCountD=initializeCountDicts()
    for i in orfL:
        x = 0
        while(x<len(i)):
            if(x<len(i)-3):
                codonCountD[i[x:x+3]] = codonCountD[i[x:x+3]] + 1
            if(x<=(len(i) - 6)):
                twoCodonCountD[i[x:x+6]] =  twoCodonCountD[i[x:x+6]] + 1
            x = x + 3
    return codonCountD,twoCodonCountD

def condProb(orfL):
    codonCountD,twoCodonCountD = count(orfL)
    for i in twoCodonCountD:
        if(codonCountD[i[0:3]]>0):
            twoCodonCountD[i] = twoCodonCountD[i]/codonCountD[i[0:3]]
        else:
            twoCodonCountD[i] = 0
    return twoCodonCountD

def logLikelihoodRatioSum(orf,llrD):
    total = 0;
    x = 0
    while(x<len(orf) - 5):
        total = total + llrD[orf[x:x+6]]
        x = x + 3
    return total
def predict(orfL,llrD):
    codingL = []
    noncodingL = []
    for i in orfL:
        if(logLikelihoodRatioSum(i,llrD) > 0):
            codingL += [i]
        else:
            noncodingL += [i]
    return codingL,noncodingL
