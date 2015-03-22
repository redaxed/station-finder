__author__ = 'daxx'
from flask import Flask,render_template
app = Flask(__name__)
import json

categories = ["Spanish", "Christian", "Talk Radio", "Contemporary", "News", "Classical", "Sports", "Hits", "Alternative", "Oldies", "Jazz"]

@app.route('/')
def hello_world():
    return render_template("index.html", categories=categories)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True,debug=True)