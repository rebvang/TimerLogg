import json
import plottf
import other_types as ot

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

plottf.lag_plott(data, typ="Totalt")

with open("fag_farger.json", "r", encoding="utf-8") as fil:
    farger = json.load(fil)

for fag, farge in farger.items():
    nydata = [i for i in data if i['subject'] == fag]
    plottf.lag_plott(nydata, typ=fag, farge=farge)

with open("type_farger.json", "r", encoding="utf-8") as fil:
    farger = json.load(fil)

for n, v in farger.items():
    nydata = [i for i in data if i['type'] == n]
    plottf.lag_plott(nydata, typ=n, farge=v)

farger = ot.main()
for n, v in farger.items():
    nydata = [i for i in data if i['type'] in n]
    plottf.lag_plott(nydata, typ=n, farge=v)
