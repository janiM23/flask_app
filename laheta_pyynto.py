import requests
import json

mittaus = {"x": 6,"y": 12}

while(True):
    mittaus["x"] = int(input("Anna viikonpäivä: "))
    mittaus["y"] = int(input("Anna lämpötila: "))

    viesti = json.dumps(mittaus)
    # /api on mistä voi tarkastella. /lisaa jos halutaan survoa tietoa johonkin
    vastaus = requests.post('http://127.0.0.1:5000/lisaakantaan', data=viesti)

