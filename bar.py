import json
import plottf

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

plottf.lag_plott(data, typ="Totalt")
