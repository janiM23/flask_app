from flask import Flask, render_template, request
import json

app = Flask(__name__)

lampotilat = [
    {'x':1, 'y':14},
    {'x':2, 'y':23},
    {'x':3, 'y':18}
]

paivat = ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai']

# kirjoita selaimeen localhost:5000/api, että voit tarkastella sivua
@app.route('/api', methods=['GET'])
def index():
    return render_template("mittaukset.html", taulukko=lampotilat, paivat=paivat)

@app.route('/lisaa', methods=['POST'])
def lisaa():
    uusimittaus = request.get_json(force=True)
    lampotilat.append(uusimittaus)
    return(json.dumps(uusimittaus))

if __name__ == "__main__":
    app.run(debug=True)