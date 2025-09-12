import json
import matplotlib.pyplot as plt
import datetime
import sys
import matplotlib.patches as mpatches
import subprocess
from mylib import all_false

with open("fag_farger.json", "r", encoding="utf-8") as fil:
    farger = json.load(fil)


leg_patch = dict()
for fag, farge in farger.items():
    leg_patch[fag] = mpatches.Patch(color=farge, label=fag)

fagleg = [i.lower() for i, n in farger.items()]
leg = dict()


with open("logg.json", "r") as fil:
    data = json.load(fil)


start_kl = 4
slutt_kl = start_kl + 20

start_uke = int(sys.argv[1])
slutt_uke = int(sys.argv[2]) + 1


missing = set()

for uke_nr in [i for i in range(start_uke, slutt_uke)]:
    for i in fagleg:
        leg[i] = False
    ukedager = [
        (datetime.date.fromisocalendar(2025, uke_nr, d).isoformat())
        for d in range(1, 8)  # ISO weekday: Monday=1 … Sunday=7
    ]

    plt.figure(figsize=(10, 7))
    plt.ylim(slutt_kl, start_kl)
    plt.xlim(0, 8)
    plt.grid(zorder=0)

    for i in data:
        if i['date'] in ukedager:
            d = datetime.date.fromisoformat(i['date'])
            idx = d.weekday()
            start = i['start'].split(":")
            start_idx = int(start[0]) + int(start[1])/60 # - (start_kl)
            slutt = i['end'].split(":")
            slutt_idx = int(slutt[0]) + int(slutt[1])/60 # - (start_kl)
            hoyde = (slutt_idx - start_idx)
            fag = "k"
            if i['subject'] in farger:
                fag = farger[i['subject']]
                leg[i['subject'].lower()] = True
            else:
                missing.add(i['subject'])
            rect = mpatches.Rectangle((idx+0.525, start_idx), 0.9725, hoyde, facecolor=fag, zorder=2)
            plt.gca().add_patch(rect)

    legend = [leg_patch[n.upper()] for n, v in leg.items() if v]
    plt.title(f"Uke {uke_nr}: {ukedager[0]} — {ukedager[-1]}")
    plt.yticks([i for i in range(start_kl, slutt_kl+1)])
    plt.xticks([i for i in range(9)], ["", "Man", "Tir", "Ons", "Tor", "Fre", "Lør", "Søn", ""])
    plt.legend(handles=legend)
    plt.show()

    print(missing)