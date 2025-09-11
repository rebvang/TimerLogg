import sys
import json
import plottf

fag = sys.argv[1]
if len(sys.argv) > 2:
    farge = sys.argv[2]
else:
    farge = ""

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

data = [i for i in data if i['subject'] == fag]

plottf.lag_plott(data, typ=fag, farge=farge)
