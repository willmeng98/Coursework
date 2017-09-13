from hivDist import *
from njHelper import *

def nodeSep(node,nodeL,distD):
    '''A measure of the separation between a node of interest and
    the other nodes.'''
    distSum=0
    for iternode in nodeL:
        if node != iternode:
            distSum+=distD[(node,iternode)]
    return(float(distSum)/(len(nodeL)-2))

def njMetric(node1,node2,nodeL,distD):
    '''Calculates the neighbor joining metric between two nodes.'''
    d=distD[(node1,node2)]
    s1=nodeSep(node1,nodeL,distD)
    s2=nodeSep(node2,nodeL,distD)
    return(d-s1-s2)

def branchLength(nodeA,nodeB,nodeL,distD):
    '''Takes two nodes we're planning to merge, nodeA and nodeB. Calculates the
branch lengths from their common ancestor to each.'''
    dist=distD[(nodeA,nodeB)]
    sepA=nodeSep(nodeA,nodeL,distD)
    sepB=nodeSep(nodeB,nodeL,distD)
    branchA=0.5*(dist+(sepA-sepB))
    branchB=0.5*(dist+(sepB-sepA))
    return(branchA,branchB)

def bestPair(nodeL,distD):
    node1 = nodeL[0]
    node2 = nodeL[1]
    for i in range(0,len(nodeL)-1):
        for k in range(i+1,len(nodeL)):
            if(njMetric(nodeL[i],nodeL[k],nodeL,distD)<njMetric(node1,node2,nodeL,distD)):
                node1 = nodeL[i]
                node2 = nodeL[k]
    return node1,node2

def mergeNodes(nodeA,nodeB,branchLenA,branchLenB):
    node1 = (nodeA[0], nodeA[1], nodeA[2], branchLenA)
    node2 = (nodeB[0], nodeB[1], nodeB[2], branchLenB)
    return ('anc',node1,node2,0)

def updateDistances(nodeA,nodeB,newNode,nodeL,distD):
    for i in nodeL:
        if((i != nodeA) and (i != nodeB)):
            distD[i,newNode] = 0.5 * (distD[i,nodeA] + distD[i,nodeB] - distD[nodeA,nodeB])
            distD[newNode,i] = 0.5 * (distD[i,nodeA] + distD[i,nodeB] - distD[nodeA,nodeB])

    return distD

def terminate(nodeL,distD):
    nodeA,nodeB = nodeL
    dist = distD[nodeA,nodeB]
    node1 = (nodeA[0], nodeA[1], nodeA[2], dist/2)
    node2 = (nodeB[0], nodeB[1], nodeB[2], dist/2)
    return ('anc',node1,node2,0)

def nj(nodeL,distD):
    while(len(nodeL) > 2):
        pair1,pair2 = bestPair(nodeL,distD)
        distance = branchLength(pair1, pair2, nodeL, distD)
        mergednode = mergeNodes(pair1,pair2,distance[0],distance[1])
        distD = updateDistances(pair1,pair2,mergednode,nodeL,distD)
        nodeL.remove(pair1)
        nodeL.remove(pair2)
        nodeL.append(mergednode)
    return terminate(nodeL,distD)





            




