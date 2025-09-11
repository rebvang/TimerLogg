import sys
import json
import plottf

typer = ["Forelesning", "Video", "Alene", "\u00d8vingstime", "Obligatorisk arbeid", "Eksamen", "Podcast"]
farger = ["#000000",  "#0000ff", "#ff0000", "#00ff00",       "#00aaaa",             "#888888", "#000077"]

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

if len(typer) != len(farger):
    raise ValueError

for n in range(len(typer)):
    nydata = [i for i in data if i['type'] == typer[n]]
    plottf.lag_plott(nydata, typ=typer[n], farge=farger[n])

nydata = [i for i in data if (i['type'] == "Alene") or (i['type'] == "Obligatorisk arbeid")]
plottf.lag_plott(nydata, typ="Alene + Obligatorisk Arbeid", farge="#ff33ff")
