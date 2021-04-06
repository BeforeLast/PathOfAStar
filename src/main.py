from graph import *
from flask import Flask , render_template , request
# import matplotlib.pyplot as plt
# import networkx as nx

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisjustsomesecretkey'

G = Graph()
gInfo = []
@app.route('/', methods=['GET', 'POST'])
def main() :
    return render_template("map.html", names = [], coords = [], dist = 0 , graphInfo = [])

@app.route('/load-file/', methods=['GET', 'POST'])
def loadFile() :
    fileNamePath = request.form['test']
    print(fileNamePath)
    G.fillGraphWithFile(fileNamePath)
    gInfo = G.toArray()
    # print(G.toArray())
    return render_template("map.html", names = [], coords = [], dist = 0 , graphInfo = gInfo)

@app.route('/calculate-route/', methods=['GET', 'POST'])
def calculateRoute(startNode,goalNode):
    pathNames, pathDist, pathSuccess = G.AStar(startNode,goalNode)
    if (pathSuccess) :
        pathCoords = []
        for i in range(len(pathNames)) :
            currLoc = []
            currLoc.append(G.getNodeLoc(pathNames[i]).x)
            currLoc.append(G.getNodeLoc(pathNames[i]).y)
            pathCoords.append(currLoc)
        return render_template("map.html", coords = pathCoords, dist = pathDist , graphInfo = gInfo)
    else:
        return render_template("map.html", coords = [], dist = 0 , graphInfo = gInfo)

if __name__ == '__main__':
    app.run(debug=True)