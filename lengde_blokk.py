import json
import matplotlib.pyplot as plt

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

with open("type_farger.json", "r", encoding="utf-8") as fil:
    farger = json.load(fil)

nydata = []
not_want = ["Eksamen", "Forelesning", "\u00d8vingstime"]
for i in data:
    if i['pause'] == 0 and i['type'] not in not_want:
        nydata.append(i)
data = nydata[:]

for i in not_want:
    del farger[i]

xvalues = [""]

plt.figure()
for n, v in farger.items():
    nydata = [i for i in data if i['type'] == n]
    y = [i['timeSpent'] for i in nydata]
    if n not in xvalues:
        xvalues.append(n)
    x = xvalues.index(n)
    for i in y:
        plt.plot(x, i, "o", color=v)

xlabels1 = xvalues + [""]
xlabels = []
for i in xlabels1:
    if i == "Studass Forberedelse":
        xlabels.append("LA prep")
        continue
    if i == "Obligatorisk arbeid":
        xlabels.append("Obl. Arb.")
        continue
    xlabels.append(i)
plt.xticks(list(range(0, len(xlabels))), xlabels)#, rotation=-30)
plt.grid()
plt.title("I don't fucking know")
plt.ylabel("Minutter")
plt.xlabel("Type")
plt.show()
