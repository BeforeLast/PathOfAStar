from graph import *
from flask import Flask , render_template
# import matplotlib.pyplot as plt
# import networkx as nx

G = Graph()
G.fillGraphWithFile("../test/test6.txt")

# Gnx = nx.Graph()
# for node in G.nodes :
#     Gnx.add_node(node.name)

# nx.draw(Gnx, with_labels=True, font_weight='bold')
# plt.show()

# show the list of node names
print("Nama-nama node yang terdefinisi di graf :")
for node in G.nodes :
    print(node.name)

# input the start and end nodes
print("---------------------------------")
startNode = input("Masukkan nama node asal : ")
endNode = input("Masukkan nama node tujuan : ")

# get the pathNames, pathCoords, pathDist
print("--------- HASIL A* PATH ---------")
pathNames, pathDist, pathSuccess = G.AStar(startNode,endNode)
if (pathSuccess) :
    pathCoords = []
    for i in range(len(pathNames)) :
        currLoc = []
        currLoc.append(G.getNodeLoc(pathNames[i]).x)
        currLoc.append(G.getNodeLoc(pathNames[i]).y)
        pathCoords.append(currLoc)

    # initiate flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisjustsomesecretkey'

    @app.route('/', methods=['GET', 'POST'])
    def main() :
        return render_template("map.html", names = pathNames, coords = pathCoords, dist = pathDist)

    # run the flask
    if __name__ == '__main__':
        app.run(debug=False)
