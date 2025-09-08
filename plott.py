import json
import matplotlib.pyplot as plt
import datetime
import sys
import matplotlib.patches as mpatches
import subprocess

def all_false(n):
    return (False for i in range(n))

MAT300 = mpatches.Patch(color='#00aaff', label='MAT300')
MOD300 = mpatches.Patch(color='#ff0000',  label='MOD300')
DAT120 = mpatches.Patch(color="#00cc00",  label='DAT120')
DAT320 = mpatches.Patch(color="#7700aa",  label='DAT320')
DAT330 = mpatches.Patch(color="#f7ff03",  label='DAT330')
STA100 = mpatches.Patch(color="#0020ff",  label='STA100')
ELE320 = mpatches.Patch(color="orange",  label='ELE320')
WIN100 = mpatches.Patch(color="#0000aa",  label='WIN100')

fagleg = ["mat300", "mod300", "dat120", "dat320", "dat330", "sta100", "ele320", "win100"]
leg = dict()
for i in fagleg:
    leg[i] = False

with open("logg.json", "r") as fil:
    data = json.load(fil)

uke_nr = int(sys.argv[1])
ukedager = [
    (datetime.date.fromisocalendar(2025, uke_nr, d).isoformat())
    for d in range(1, 8)  # ISO weekday: Monday=1 … Sunday=7
]

start_kl = 4
slutt_kl = start_kl + 20

uke = [["" for _ in range((slutt_kl-start_kl)*60)] for _ in range(7)]
# dag = ["" for _ in range(6*60)]

missing = set()

for i in data:
    if i['date'] in ukedager:
        d = datetime.date.fromisoformat(i['date'])
        idx = d.weekday()
        start = i['start'].split(":")
        start_idx = int(start[0])*60 + int(start[1]) - (start_kl * 60)
        slutt = i['end'].split(":")
        slutt_idx = int(slutt[0])*60 + int(slutt[1]) - (start_kl * 60)
        fag = "k"
        match i['subject']:
            case "MOD300":
                fag = "#ff0000"
                leg["mod300"] = True
            case "MAT300":
                fag = "#00aaff"
                leg["mat300"] = True
            case "DAT120":
                fag = "#00cc00"
                leg["dat120"] = True
            case "DAT320":
                fag = "#7700aa"
                leg["dat320"] = True
            case "DAT330":
                fag = "#f7ff03"
                leg["dat330"] = True
            case "STA100":
                fag = "#0020ff"
                leg["sta100"] = True
            case "ELE320":
                fag = "orange"
                leg["ele320"] = True
            case "WIN100":
                fag = "#0000aa"
                leg["win100"] = True
            case _:
                missing.add(i['subject'])
        for n in range(start_idx, slutt_idx):
            uke[idx][n] = fag

legend = [globals()[n.upper()] for n, v in leg.items() if v]


# Just plot a line for each minute?? y = time. x + dx = day.

plt.figure(figsize=(10, 7))
plt.ylim(slutt_kl, start_kl)
plt.xlim(0, 8)
plt.grid()

for i, dag in enumerate(uke):
    for idx, fag in enumerate(dag):
        if fag != "":
            y = start_kl + idx*(1/60)
            x1, x2 = i+0.525, i+1.4975 # Give some space between so adjacent days don't overlap
            plt.plot([x1, x2], [y, y], fag)

plt.title(f"Uke {uke_nr}: {ukedager[0]} — {ukedager[-1]}")
plt.yticks([i for i in range(start_kl, slutt_kl+1)])
plt.xticks([i for i in range(9)], ["", "Man", "Tir", "Ons", "Tor", "Fre", "Lør", "Søn", ""])
plt.legend(handles=legend)
plt.show()

print(missing)