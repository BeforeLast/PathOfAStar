from graph import *
from flask import Flask , render_template , request
# import matplotlib.pyplot as plt
# import networkx as nx
HTML_TEMPLATE = "map.html"

def printDefaultTemplate(graphInfo=[]):
    return render_template(HTML_TEMPLATE, route = "", coords = [], dist = 0 , graphInfo = graphInfo)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisjustsomesecretkey'

G = Graph()
gInfo = []
@app.route('/', methods=['GET', 'POST'])
def main() :
    return printDefaultTemplate()

@app.route('/load-file/', methods=['GET', 'POST'])
def loadFile() :
    fileNamePath = request.form['test']
    if (len(fileNamePath)==0):
        return printDefaultTemplate()
    print("SELECTED FILE =",fileNamePath)
    G.fillGraphWithFile(fileNamePath)
    gInfo = G.toArray()
    return printDefaultTemplate(gInfo)

@app.route('/calculate-route/', methods=['GET', 'POST'])
def calculateRoute():
    startNode = request.form.get("startNodeName")
    goalNode = request.form.get("goalNodeName")
    if startNode==None or goalNode==None:
        return printDefaultTemplate()
    pathNames, pathDist, pathSuccess = G.AStar(startNode,goalNode)
    gInfo = G.toArray()
    if (pathSuccess) :
        pathCoords = []
        for i in range(len(pathNames)) :
            currLoc = [G.getNodeLoc(pathNames[i]).x, G.getNodeLoc(pathNames[i]).y]
            pathCoords.append(currLoc)
        routeResult = '-'.join(pathNames)
        return render_template(HTML_TEMPLATE, route = routeResult, coords = pathCoords, dist = pathDist , graphInfo = gInfo)
    else:
        badRouteResult = "No path found from " + startNode + " to " + goalNode
        return render_template(HTML_TEMPLATE, route = badRouteResult, coords = [], dist = 0 , graphInfo = gInfo)

if __name__ == '__main__':
    app.run(debug=True)