import math

class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Node :
    def __init__(self, name, point) :
        self.name = name
        self.point = point

class Edge :
    def __init__(self, startNode, endNode, dist) :
        self.startNode = startNode
        self.endNode = endNode
        self.dist = dist

class Graph :
    def __init__(self) :
        self.nodes = []
        self.edges = []

    # add a node to the graph
    def addNode(self, node) :
        self.nodes.append(node)

    # add an edge to the graph
    def addEdge(self, edge) :
        self.edges.append(edge)

    # returns an array of nodes adjancing the referenced node
    def getAdjacents(self, node) :
        res = []
        for edge in edges :
            if edge.startNode is node :
                res.append(edge.endNode)
            if edge.endNode is node :
                res.append(edge.startNode)
        return res

    # fill the graph from an input file
    def fillGraphWithFile(self, fileName) :
        f = open(fileName,"r")
        readOut = f.readlines()

        nodeCount = int(readOut[0].replace('\n',''))

        # fill the nodes
        for i in range (1,nodeCount+1) :
            line = readOut[i].replace('\n','').split(' ')
            P = Point(float(line[1]) , float(line[2]))
            N = Node(line[0], P)
            self.addNode(N)

        # fill the edges
        for i in range(nodeCount+1, nodeCount*2+1) :
            line = readOut[i].replace('\n','').split(' ')
            N1 = self.nodes[i-nodeCount-1]
            for j in range(nodeCount) :
                if (line[j] == '1') and (i-nodeCount-1 < j) :
                    N2 = self.nodes[j]
                    dist = math.sqrt(math.pow(N2.point.x - N1.point.x, 2) + math.pow(N2.point.y - N1.point.y, 2))
                    E = Edge(N1,N2,dist)
                    self.addEdge(E)

        f.close()