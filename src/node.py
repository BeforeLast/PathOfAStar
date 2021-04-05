from location import *

class Node :
    def __init__(self, name, location) :
        self.name = name
        self.location = location
        self.adjacentNode = []

    # add adjacent node name
    # input
    #   string : nodeName
    # I.S. : self.adjacentNode == [..]
    # F.S. : self.adjacentNode == [..,nodeName]
    def addAdjNode(self,nodeName):
        self.adjacentNode.append(nodeName)