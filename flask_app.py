from flask import Flask, render_template, request
import json
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("mittaukset.db3")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mittaukset (id INTEGER PRIMARY KEY, paiva INTEGER, mittaus INTEGER)")
con.commit()
con.close

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

@app.route('/lisaakantaan', methods=['POST'])
def lisaa_tietokantaan():
    uusimittaus = request.get_json(force=True)

    con = sqlite3.connect("mittaukset.db3")
    cur = con.cursor()
    cur.execute("INSERT INTO mittaukset (paiva, mittaus) VALUES (?,?)", [uusimittaus["x"], uusimittaus["y"]])
    con.commit()
    con.close
    return(json.dumps(uusimittaus))

# hakee tietokannasta tiedot näytettäväksi sivulle
@app.route('/api/haekannasta', methods=['GET'])
def hae_tietokannasta():
    con = sqlite3.connect("mittaukset.db3")
    cur = con.cursor()
    cur.execute("SELECT paiva, mittaus FROM mittaukset")

    # hakee datan tiedot-muuttujaan
    tiedot = cur.fetchall()
    
    kantatiedot = list()

    # for-looppi, missä tiedot kerätään tiedot-tietokannasta ja lisätään
    # kantatiedot-listaan
    for paiva in tiedot:
        temp = dict(x=paiva[0], y=paiva[1])
        kantatiedot.append(temp)
    
    con.commit()
    con.close()

    return render_template("mittaukset.html", taulukko=kantatiedot, paivat=paivat)

if __name__ == "__main__":
    app.run(debug=True)