from graph import *

G = Graph()
G.fillGraphWithFile("../test/test1.txt")

G.AStar('D','A')