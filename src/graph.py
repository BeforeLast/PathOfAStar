import math
from typing import overload
from location import *
from node import *
from prioqueue import *

EARTH_CIRCUMFERENCE = 40007863

class Graph :
    def __init__(self) :
        self.nodes = []

    # add a node to the graph
    # input
    #   Node : node
    # I.S. : nodes == [..]
    # F.S. : nodes == [..,node]
    def addNode(self, node) :
        self.nodes.append(node)
    
    # convert graph to array
    # output : [[[nodeName, location],..],[[[edgeSrcLoc.x, edgeSrcLoc.y], [edgeTrgLoc.x, edgeTrgLoc.y]],..]]]
    def toArray(self):
        nodeList = []
        edgeList = []
        for node in self.nodes:
            
            tempNodeArr = [node.name, node.location.x, node.location.y]
            nodeList.append(tempNodeArr)

            adjNode = node.adjacentNode.copy()

            tempNodeLoc = node.location
            for adjNodeName in adjNode:
                tempAdjLoc = self.getNodeLoc(adjNodeName)
                if ([[tempNodeLoc.x, tempNodeLoc.y],[tempAdjLoc.x,tempAdjLoc.y]] not in edgeList) and ([[tempAdjLoc.x,tempAdjLoc.y],[tempNodeLoc.x, tempNodeLoc.y]] not in edgeList):
                    edgeList.append([[tempNodeLoc.x, tempNodeLoc.y], [tempAdjLoc.x,tempAdjLoc.y]])
        
        return [nodeList,edgeList]

    # get node with the name of nodeName
    # input
    #   nodeName : string
    # output : Location
    def getNode(self, nodeName):
        for node in self.nodes:
            if node.name == nodeName:
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
    # input 
    #   string : fileName
    # I.S. : self.nodes == [..]
    # F.S. : self.nodes == [..,newnode1,newnode2,..,newnodeN]
    def fillGraphWithFile(self, fileName) :
        self.nodes = []
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

    # get total cost from srcNodeName to trgNodeName with the goal goalNodeName
    # input 
    #   string : srcNodeName, goalNodeName
    # output : array of string, float, boolean
    def AStar(self, srcNodeName, goalNodeName):
        ## Guard
        if self.getNode(srcNodeName) == None or self.getNode(goalNodeName) == None:
            return None, None, False
        ## PriorityQueue elements as tuple index
        TOTALCOST_INDEX = 0
        CURRENTNODENAME_INDEX = 1
        VISITEDNODE_INDEX = 2

        ## PriorityQueue elements : (cost,currentNodeName,visitedNode)
        queue = PriorityQueue()

        ## PriorityQueue initialization (using start node)
        temptup = (self.calculateDistance(srcNodeName,goalNodeName),srcNodeName,[srcNodeName])
        queue.enqueue(temptup)

        while len(queue)>0 and queue.queue[0][CURRENTNODENAME_INDEX] != goalNodeName:
            currentNode = queue.dequeue() # (cost,currentNodeName,visitedNode) - (float, string, [string])

            currentAccCost = currentNode[TOTALCOST_INDEX]
            print("CURRENT COST  ", currentAccCost)
            node = self.getNode(currentNode[CURRENTNODENAME_INDEX])

            currentAccCost -= self.calculateDistance(node.name,goalNodeName)

            visitedNode = currentNode[VISITEDNODE_INDEX].copy()

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

        pathNames = []
        dist = 0.0
        success = True
                    
        if len(queue)>0: # found path from Source Node to Goal Node
            print("COST = ",end='')
            print(queue.queue[0][TOTALCOST_INDEX])
            dist = queue.queue[0][TOTALCOST_INDEX]

            print("PATH = ",end='')
            print(queue.queue[0][VISITEDNODE_INDEX][0],end='')
            pathNames.append(queue.queue[0][VISITEDNODE_INDEX][0])
            for nodeName in queue.queue[0][VISITEDNODE_INDEX][1:]:
                print('-'+nodeName,end='')
                pathNames.append(nodeName)
            print()
        
        else: # no path found from Source Node to Goal Node
            print("NO PATH FOUND")
            success = False

        return pathNames, (dist/360) * EARTH_CIRCUMFERENCE, success