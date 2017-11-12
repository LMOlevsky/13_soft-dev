from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

req = urllib2.Request("https://www.thebluealliance.com/api/v3/team/frc694/media/2017?X-TBA-Auth-Key=jlTx0fXi4VSUc8IEtgq4mNixSvBxx0H6Tmzmlk9ScTDsYPLG7N6F5MSd3gqXQJ00", headers={ 'User-Agent': 'Mozilla/5.0' })
json_str = urllib2.urlopen(req).read()
d = json.loads(json_str)


req2 = urllib2.Request("https://api.nasa.gov/planetary/apod?api_key=o8PHFoXwiKZ4W4gafFk2VV1JaxxyMGzuhXSjToQ8", headers={ 'User-Agent': 'Mozilla/5.0' })
json_str2 = urllib2.urlopen(req2).read()
d2 = json.loads(json_str2)

@app.route("/", methods=['POST', 'GET'])
def root():
    return render_template("temp.html", tba=d[3]["details"]["thumbnail_url"], nasa=d2["url"])


if __name__ == '__main__':    
    app.debug = True
    app.run()
