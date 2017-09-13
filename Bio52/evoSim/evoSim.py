import random
from Org import *

def procreate(orgL,popSize,mutProb):
	neworglist = []
	for i in range(0,popSize):
		neworglist += [random.choice(orgL).replicate(mutProb)]
	return neworglist

def evoSim(popL, popSize, numGen, mutProb):
	genlist = [procreate(popL,popSize,mutProb)]
	for i in range(1,numGen + 1):
		genlist += [procreate(genlist[i-1],popSize,mutProb)]
	return genlist

def evoSimSelect(popL,popSize,numGen,mutProb,fitnessD):
	genlist = [procreate(cullPop(popL,fitnessD),popSize,mutProb)]
	for i in range(1,numGen + 1):
		genlist += [procreate(cullPop(genlist[i-1],fitnessD),popSize,mutProb)]
	return genlist



