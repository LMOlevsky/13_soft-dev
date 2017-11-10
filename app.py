from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

u = urllib2.urlopen("https://api.nasa.gov/planetary/earth/imagery?lon=-74.013871&lat=40.717984&date=2017-02-01&cloud_score=False&api_key=o8PHFoXwiKZ4W4gafFk2VV1JaxxyMGzuhXSjToQ8")

U = u.read()

rest = json.loads(U)

@app.route("/", methods=['POST', 'GET'])
def root():
    return render_template("temp.html", things=rest["url"])


if __name__ == '__main__':    
    app.debug = True
    app.run()
