import json
import filterf
from datetime import datetime, timedelta
from gen_funk import plott_x_y, add_datetime_and_sort

M = 7

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

data = add_datetime_and_sort(data)

min_date = datetime.strptime(data[0]['date'], "%Y-%m-%d") - timedelta(days=1)
max_date = datetime.strptime(data[-1]['date'], "%Y-%m-%d") + timedelta(days=1)
all_dates = []
current = min_date
while current <= max_date:
    all_dates.append(current)
    current += timedelta(days=1)

x = [d.strftime("%Y-%m-%d") for d in all_dates]
y = [0 for _ in range(len(x))]

for i in data:
    idx = x.index(i['date'])
    y[idx] += i['timeSpent']/60

y = filterf.FIR(y, M)

plott_x_y(all_dates, y, "#000000", f"Totalt tid brukt — FIR-filtrert m/ M = {M}")