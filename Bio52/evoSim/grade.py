import unittest
import evoSim as hw

class SimpleTests(unittest.TestCase):

    def testB(self):
        # procreate
        orgL=hw.startingPop('AAA',3)
        newOrgL=hw.procreate(orgL,5,0)
        self.assertTrue(len(newOrgL)==5,msg="problem in procreate.")
        self.assertTrue(all([isinstance(o,hw.org) for o in newOrgL]),msg="problem in procreate.")
        
    def testC(self):
        # procreate
        orgL=hw.startingPop('AAA',3)
        newOrgL=hw.procreate(orgL,5,0) # mutProb 0
        self.assertTrue(all([o.dna=='AAA' for o in newOrgL]),msg="problem in procreate.")
        newOrg2L=hw.procreate(orgL,30,1) # mutProb 1
        self.assertTrue(any([not o.dna=='AAA' for o in newOrg2L]),msg="problem in procreate.")


    def testD(self):
        popSize=3; numGen=5
        popL=hw.startingPop('AAA',3)
        simL=hw.evoSim(popL,3,5,0)
        self.assertTrue(len(simL)==numGen+1,msg="problem in evoSim.")

    def testE(self):
        popSize=3; numGen=5
        popL=hw.startingPop('AAA',3)
        simL=hw.evoSim(popL,popSize,numGen,0)
        for popL in simL:
            self.assertTrue(len(popL)==popSize,msg="problem in evoSim.")
            self.assertTrue(all([isinstance(o,hw.org) for o in popL]),msg="problem in evoSim.")

    def testF(self):
        popL=hw.startingPop('AAA',2)+hw.startingPop('CCC',2)
        exampleFitD2={'K':1, 'P':.6}
        popSize=4; numGen=5
        simL=hw.evoSimSelect(popL,popSize,numGen,0,exampleFitD2)
        self.assertTrue(len(simL)==numGen+1,msg="problem in evoSimSelect.")
        for popL in simL:
            self.assertTrue(len(popL)==popSize,msg="problem in evoSimSelect.")
            self.assertTrue(all([isinstance(o,hw.org) for o in popL]),msg="problem in evoSimSelect.")
        
def arePopsSame(L1,L2):
    '''Return True if populations are same.'''
    if len(L1) != len(L2): return False
    else:
        L1.sort()
        L2.sort()
        for i in range(len(L1)):
            if L1[i].dna != L2[i].dna:
                return False
        return True

def isPopUniform(popL):
    dna=popL[0].dna
    for org in popL:
        if org.dna != dna:
            return False
    return True


if __name__ == '__main__':
    unittest.main()
