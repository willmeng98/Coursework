from evoSim import *
import matplotlib.pyplot as pyplot

def calcAlleleProportions(allele,simL):
    '''Calculate the proportion of allele in each generation of the
simulation give by simL.'''
    propL=[]
    popSize=len(simL[0])
    for popL in simL:
        alCt=0
        for org in popL:
            if org.dna==allele:
                alCt+=1
        propL.append(float(alCt)/popSize)
    return propL
        
def plot2alleleSim(popSize,numGen,numReps,selectOn):
    '''Run simulations and create drift plots for the case of a starting
population with equal numbers of two alleles and no mutation.'''
    for i in range(numReps):
        # create starting pop with two equal frequency alleles
        A1='AAA'
        A2='CCC'
        mutProb=0
        popL=startingPop(A1,int(popSize/2))+startingPop(A2,int(popSize/2))
        if selectOn:
            simL=evoSimSelect(popL,popSize,numGen,mutProb,{'K':1, 'P':.85})
        else:
            simL=evoSim(popL,popSize,numGen,mutProb)
        propL=calcAlleleProportions(A1,simL)
        pyplot.plot(propL,'b')

    #pyplot.xlabel("generation")
    pyplot.ylabel(A1+" allele frequency")
    pyplot.ylim((0,1))

def nucCount(popL,site):
    '''Calculate the counts of A, C, G, and T at genome index site in the
genomes of organisms in popL.'''
    countL=[0,0,0,0]
    for i in range(len(popL)):
        if popL[i].dna[site]=="A": countL[0]+=1
        elif popL[i].dna[site]=="C": countL[1]+=1
        elif popL[i].dna[site]=="G": countL[2]+=1
        elif popL[i].dna[site]=="T": countL[3]+=1
    return countL

def heterozygositySite(popL,site):
    '''Calculate heterozygosity at site.'''
    countL=nucCount(popL,site)
    numSites=len(popL)
    propHomozyg=0.0
    for ct in countL:
        propHomozyg+=(float(ct)/numSites)**2
    return 1-propHomozyg

def heterozygosity(popL):
    '''Calculate heterozygosity, the probability of drawing two
different alleles, sampling with replacement.'''
    hetSum=0
    for i in range(popL[0].dnaLen):
        hetSum+=heterozygositySite(popL,i)
    return float(hetSum)/popL[0].dnaLen

def heterozygositySim(simL):
    '''Calculate heterozygosity for each generation in a simulation and
return in list.'''
    heteroL=[]
    for popL in simL:
        heteroL.append(heterozygosity(popL))
    return heteroL
    
def plotMutationSim(startAllele,popSize,numGen,mutProb,numReps,selectOn,fitnessD,col):
    '''Run simulations, then calculate and plot heterozygosity.'''
    heteroLL=[]
    for i in range(numReps):
        popL=startingPop(startAllele,popSize)
        if selectOn:
            simL=evoSimSelect(popL,popSize,numGen,mutProb,fitnessD)
        else:
            simL=evoSim(popL,popSize,numGen,mutProb)
        
        heteroLL.append(heterozygositySim(simL))
    # get average heterozygosity for each generation
    avHetL=[]
    for i in range(len(heteroLL[0])):
        hetSum=0
        for j in range(len(heteroLL)):
            hetSum+=heteroLL[j][i]
        avHetL.append(float(hetSum)/len(heteroLL))
    #print "average Heterozygosity"," ".join([format(x,".2f") for x in avHetL])
    pyplot.plot(avHetL,col)
    pyplot.ylabel("Heterozygosity")


fitnessD={'T':1,'P':.5,'A':.5,'N':.5,'K':.5,'I':.5,'M':.5}

pyplot.subplot(2, 1, 1)
plot2alleleSim(150,40,20,False)
pyplot.title("Popsize 150")
pyplot.subplot(2, 1, 2)
plot2alleleSim(1000,40,20,False)
pyplot.title("Popsize 1000")
pyplot.xlabel("generation")
pyplot.show()


