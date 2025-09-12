import json
import plottf

with open("fag_farger.json", "r", encoding="utf-8") as fil:
    farger = json.load(fil)

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

for fag, farge in farger.items():
    nydata = [i for i in data if i['subject'] == fag]
    plottf.lag_plott(nydata, typ=fag, farge=farge)
