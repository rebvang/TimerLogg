import json
import matplotlib.pyplot as plt

with open("TimerLogg/logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

x = []
y = []

for i, d in enumerate(data):
    x.append(i)
    y.append(d['pause'])

plt.figure()

plt.bar(x, y)

plt.title("Pause registrert på enkeltblokker")
plt.ylabel("Minutter")
plt.xlabel("Blokkindeks")
plt.show()
