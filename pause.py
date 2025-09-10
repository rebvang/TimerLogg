import json
import matplotlib.pyplot as plt

with open("TimerLogg/logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

x = [i for i in range(len(data))]
y = [i['pause'] for i in data]

plt.figure()

plt.bar(x, y)

plt.title("Pause registrert på enkeltblokker")
plt.ylabel("Minutter")
plt.xlabel("Blokkindeks")
plt.show()
