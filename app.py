__author__ = 'daxx'
from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
import json
import db

categories = ["Country", "Spanish", "Christian", "Talk Radio", "Contemporary", "News", "Classical", "Sports", "Hits", "Alternative", "Oldies", "Jazz"]

@app.route('/')
def hello_world():
    return render_template("index.html", categories=sorted(categories))

@app.route('/get_station_2')
def get_station():
    city = request.args.get('city')
    categories = request.args.get('categories').split(",")
    state = request.args.get('state')
    print city,state,categories
    if categories==[""]:
        categories = ["Country"]
    ls = db.get_stations_mason(city,state,categories)
    print ls
    return jsonify({"stations":[station[1] for station in ls]})

@app.route("/get_station")
def lat_long():
    lat = float(request.args.get('lat'))
    long = float(request.args.get("lng"))
    categories = request.args.get('categories').split(",")
    print "Looking up "+str(lat)+" "+str(long)+" "+categories
    ls = db.get_stations_long_lat(lat,long,categories)
    # print ls
    return jsonify({"stations":[station[1] for station in ls]})




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True,debug=True)