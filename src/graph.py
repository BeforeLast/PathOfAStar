import math
from typing import overload
from location import *
from node import *
from prioqueue import *

class Graph :
    def __init__(self) :
        self.nodes = []

    # add a node to the graph
    # input :
    #   Node : node
    # I.S. : nodes == [..]
    # F.S. : nodes == [..,node]
    def addNode(self, node) :
        self.nodes.append(node)

    # get node with the name of nodeName
    # input
    #   nodeName : string
    # output : Location
    def getNode(self, nodeName):
        for node in self.nodes:
            if node.name is nodeName:
                return node
        return None
    
    # get node location of a node with the name of nodeName
    # input
    #   nodeName : string
    # output : Location
    def getNodeLoc(self, nodeName):
        if self.getNode(nodeName) == None:
            return None
        return self.getNode(nodeName).location

    # calculate Euclidean Distance of 
    # input
    #   string : nodeName
    # output : float
    def calculateDistance(self, srcNodeName, trgNodeName):
        return self.getNodeLoc(srcNodeName).euclideanDist(self.getNodeLoc(trgNodeName))

    # get total cost from srcNodeName to trgNodeName with the goal goalNodeName
    # input 
    #   string : srcNodeName, trgNodeName, goalNodeName
    # output : float
    def calculateTotalCost(self, srcNodeName, trgNodeName, goalNodeName):
        return  self.calculateDistance(srcNodeName,trgNodeName) + self.calculateDistance(trgNodeName,goalNodeName)

    # fill the graph from an input file
    def fillGraphWithFile(self, fileName) :
        f = open(fileName,"r")
        readOut = f.readlines()

        nodeCount = int(readOut[0].replace('\n',''))

        # fill the nodes
        for i in range (1,nodeCount+1) :
            line = readOut[i].replace('\n','').split(' ')
            Loc = Location(float(line[1]) , float(line[2]))
            tempNode = Node(line[0], Loc)
            self.addNode(tempNode)

        # fill the edges
        i = 0
        for lineIdx in range(nodeCount+1, nodeCount*2+1) :
            line = readOut[lineIdx].replace('\n','').split(' ')
            for j in range(nodeCount):
                if j != i and line[j]=='1':
                    self.nodes[i].addAdjNode(self.nodes[j].name)
            i += 1
        f.close()

    def AStar(self, srcNodeName, goalNodeName):
        ## PriorityQueue elements : (cost,currentNodeName,visitedNode)
        queue = PriorityQueue()

        ## PriorityQueue initialization (using start node)
        temptup = (self.calculateDistance(srcNodeName,goalNodeName),srcNodeName,[srcNodeName])
        queue.enqueue(temptup)

        ree = 1
        while len(queue)>0 and queue.queue[0][1] != goalNodeName:
            currentNode = queue.dequeue() # (cost,currentNodeName,visitedNode) - (float, string, [string])

            currentAccCost = currentNode[0]
            node = self.getNode(currentNode[1])
            visitedNode = currentNode[2].copy()

            adjNodeNames = node.adjacentNode

            for adjNodeName in adjNodeNames:

                if (adjNodeName not in visitedNode):
                    ## create priorityQueue object to be queued into PriorityQueue queue 
                    # create total cost
                    tempAccCost = currentAccCost + self.calculateTotalCost(node.name,adjNodeName,goalNodeName)
                    
                    # create path(visited node)
                    tempVisitedNode = visitedNode.copy()
                    tempVisitedNode.append(adjNodeName)

                    # create temporary tuple
                    temptup = (tempAccCost,adjNodeName,tempVisitedNode)

                    queue.enqueue(temptup)
                    

        if len(queue)>0:
            print("COST = ",end='')
            print(queue.queue[0][0])

            print("PATH = ",end='')
            for nodeName in queue.queue[0][2]:
                print(nodeName,end='-')
        
        else: # no path found from Source Node to Goal Node
            print("NO PATH FOUND")