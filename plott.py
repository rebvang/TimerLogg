import json
import matplotlib.pyplot as plt
import datetime
import sys
import matplotlib.patches as mpatches
import subprocess
from mylib import all_false

farger = dict()
farger['MAT300'] = '#00aaff'
farger['MOD300'] = '#ff0000'
farger['DAT120'] = "#00cc00"
farger['DAT320'] = "#7700aa"
farger['DAT330'] = "#f7ff03"
farger['STA100'] = "#0020ff"
farger['ELE320'] = "orange"
farger['WIN100'] = "#0000aa"

liste = ["./script.sh"]
subprocess.run(liste)

MAT300 = mpatches.Patch(color=farger['MAT300'], label='MAT300')
MOD300 = mpatches.Patch(color=farger['MOD300'],  label='MOD300')
DAT120 = mpatches.Patch(color=farger['DAT120'],  label='DAT120')
DAT320 = mpatches.Patch(color=farger['DAT320'],  label='DAT320')
DAT330 = mpatches.Patch(color=farger['DAT330'],  label='DAT330')
STA100 = mpatches.Patch(color=farger['STA100'],  label='STA100')
ELE320 = mpatches.Patch(color=farger['ELE320'],  label='ELE320')
WIN100 = mpatches.Patch(color=farger['WIN100'],  label='WIN100')

fagleg = [i.lower() for i, n in farger.items()]
# fagleg = ["mat300", "mod300", "dat120", "dat320", "dat330", "sta100", "ele320", "win100"]
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
        if i['subject'] in farger:
            fag = farger[i['subject']]
            leg[i['subject'].lower()] = True
        else:
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