import random,numpy,scipy.stats,math
from Org import *
from evoSim import *

def allSame(seqpos,popL):
    '''Is the position seqpos the same in all orgs in popL? Return
    boolean.'''
    firstseqbase=popL[0].alleleNumT[seqpos]
    for org in popL:
        if firstseqbase != org.alleleNumT[seqpos]:
            return False
    return True

def countSubsGen(popL,lastFixBaseL,subCtL):
    '''Count substitutions in the population from one generation and add
the resulting values to subCtL.'''
    dnaLen=popL[0].dnaLen
    for pos in range(dnaLen):
        firstOrgAllele = popL[0].alleleNumT[pos] # org 0 at this gen and pos
        if firstOrgAllele !=lastFixBaseL[pos] and allSame(pos,popL):
            # we have a substitution
            lastFixBaseL[pos]=firstOrgAllele
            subCtL[pos]+=1
    return lastFixBaseL,subCtL

def countSubs(simL):
    '''Given a list containing all the generations of a simulation, count
substitutions at each nucleotide position.'''
    dnaLen=simL[0][0].dnaLen
    subCtL=[0]*dnaLen
    lastFixBaseL=[0]*dnaLen
    for gen in range(len(simL)):
        lastFixBaseL,subCtL=countSubsGen(simL[gen],lastFixBaseL,subCtL)
    return subCtL

def reformat(simLL):
    '''Each of simLL's sublists are simulation output from one
simulation. Rearrange so sublists are all values at a single
nucleotide (or codon) position.'''
    newSubL=[]
    for i in range(len(simLL[0])): newSubL.append([])
    for L in simLL:
        for i in range(len(L)):
            newSubL[i].append(L[i])
    return newSubL

def subSim(startAllele,popSize,numGens,mutProb,numReps,selectOn,fitnessD):
    '''Run evolutionary simulations which keep track of substitution rate.'''
    simLL=[]
    for rep in range(numReps):
        popL=startingPop(startAllele,popSize)
        if selectOn:
            simL=evoSimSelect(popL,popSize,numGens,mutProb,fitnessD)
        else:
            simL=evoSim(popL,popSize,numGens,mutProb)
        subCtL=countSubs(simL)
        # divide sub counts by numGens to get the av num subs per simulation per generation
        avSubsL=[float(x)/numGens for x in subCtL]
        simLL.append(avSubsL)
    subL=reformat(simLL)
    return subL

def confIntMean(L,confidence,formatString):
    '''Calculate confidence interval for the true mean of the population L
was sampled from, return as tuple of strings. Argument confidence
gives proportion of the distribution which should be contained within
the interval, e.g. 0.95 for a 95% interval.'''
    mn=numpy.mean(L)
    sd=numpy.std(L)
    if sd==0:
        return "NA","NA"
    else:
        sem=sd/math.sqrt(len(L))
        lw,hi=scipy.stats.norm.interval(confidence, loc=mn, scale=sem)
        lw=format(lw,formatString)
        hi=format(hi,formatString)
        return lw,hi
    
def printSummary(subL,formatString):
    '''Print summary of substitution rates at each position.'''
    outL=[]
    for i in range(len(subL)):
        L=subL[i]
        mn=numpy.mean(L)
        lw,hi=confIntMean(L,0.95,formatString)
        print(str(i)+" "+format(mn,formatString)+" ("+lw+"-"+hi+")")
    
## fitness dictionaries

fitnessD1={'P':1,'R':.9,'A':.9}
fitnessD2={'A':1,'L':1,'P':.7,}
