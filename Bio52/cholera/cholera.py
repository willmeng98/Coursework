from choleraData import *

def printIslands(coordsL,geneInfoL,geneCoordL):
    """For each potential island in coordsL print location and gene
    info."""
    for coords in coordsL:
        print("** Island")
        print("  chrom",geneCoordL[coords[0]][1],)
        print(geneCoordL[coords[0]][2]+"-"+geneCoordL[coords[1]-1][3])
        # print genes from coords[0] to coords[1], not including coords[1]
        for i in range(coords[0],coords[1]):
            print("  "+geneInfoL[i])
        print()

def cholera():
    hasHomologL = hasHomolog(vcN16961_vs_vcPS15,vcN16961_vs_vc2740_80,700)
    coordsL = islands(hasHomologL,12)
    printIslands(coordsL,vcN16961geneInfoL,vcN16961geneCoordL)

def hasHomolog(mat1,mat2,threshold):
	greatest = []
	for i in range(0,len(mat1)):
		greatestint = -100000
		for k in mat1[i]:
			if k > greatestint:
				greatestint = k
		for l in mat2[i]:
			if l > greatestint:
				greatestint = l
		greatest += [greatestint]
	for z in range(0,len(greatest)):
		if greatest[z] >= threshold:
			greatest[z] = 1
		else:
			greatest[z] = 0
	return greatest

def tuplesize(atuple):
	return atuple[1] - atuple[0]

def islands(hasHomologL,minSize):
	thelist = []
	i = 0;
	while(i + minSize < len(hasHomologL)):
		#print("index " + i)
		if (hasHomologL[i] == 0):
			found = 1
			for z in range(i,i+minSize):
				if(hasHomologL[z] == 1):
					found = 0
					#print(z)
			if(found == 1):
				x = i + minSize
				while(found == 1):
					if(x >= len(hasHomologL)):
						found = 0
						thelist += [(i,x)]
						i = x
						#print(i + x)
					elif(hasHomologL[x] == 1):
						found = 0
						thelist += [(i,x)]
						i = x
					x = x + 1
		i = i + 1
	#=== have unordered list
	for k in range(0,len(thelist) - 1): #sort
		thenumber = tuplesize(thelist[k])
		for l in range(k + 1,len(thelist)):
			if(tuplesize(thelist[l]) > thenumber):
				temp = thelist[k]  #swap
				thelist[k] = thelist[l]
				thelist[l] = temp

	return thelist



# i = i +
m1=[[3,6,6,7],
    [2,2,4,3],
    [4,6,5,10]]
m2=[[1,3,4,1],
    [2,4,3,1],
    [8,5,6,1]]


