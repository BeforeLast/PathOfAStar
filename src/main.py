from graph import *
# from flask import Flask , render_template

G = Graph()
G.fillGraphWithFile("../test/test2.txt")

G.AStar("KantorPos","GrandYogyaKepatihan")

# # initiate flask
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'thisisjustsomesecretkey'

# @app.route('/', methods=['GET', 'POST'])
# def displayMap() :
#     # this should be the result of the pathing, to pass to js
#     points = [[3.5898427621175326, 98.6483296391956], [3.5988800872318683, 98.65249242731477], [3.60012217704572, 98.64172067661467], [3.6062845004961233, 98.65024132694683]]
#     paths = ["Rumah Bije", "SinggahA", "SinggahB", "Rumah Doi"]
#     distance = 6969.69
#     return render_template("map.html", points = points, paths = paths, dist = distance)

# # run the flask
# if __name__ == '__main__':
#     app.run(debug=False)
