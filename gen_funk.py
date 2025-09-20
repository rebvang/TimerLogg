import matplotlib.pyplot as plt
from datetime import datetime

def plott_x_y(x, y, farge, title):
    plt.figure()
    plt.grid()
    plt.plot(x, y, "o-", color=farge)
    if isinstance(x[0], datetime):
        plt.xticks(rotation=20)
    plt.title(title)
    plt.show()

def add_datetime_and_sort(data):
    for i in data:
        string = i['date'] + "T" + i['start'] + ":00Z"
        i['time'] = datetime.strptime(string, "%Y-%m-%dT%H:%M:%SZ")
    return sorted(data, key=lambda x: x['time'])