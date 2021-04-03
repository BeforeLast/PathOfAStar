from graph import *

G = Graph()
G.fillGraphWithFile("../test/test1.txt")

for node in G.nodes :
    print(node.name + " " + str(node.point.x) + " " + str(node.point.y))
for edge in G.edges :
    print(edge.startNode.name + " " + edge.endNode.name + " " + str(edge.dist))