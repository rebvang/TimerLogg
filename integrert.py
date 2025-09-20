import json
from datetime import datetime, date, timedelta
import other_types as ot
from gen_funk import plott_x_y, add_datetime_and_sort
import filterf
import sys

if len(sys.argv) > 1:
    filtrer = True
    alfa = float(sys.argv[1])
else:
    filtrer = False

def sort_and_add_datetime(data, thing_to_plot, typ):
    nydata = [i for i in data if i[typ] in thing_to_plot]
    return add_datetime_and_sort(nydata)

def get_all_dates(min_date, max_date):
    all_dates = []
    current = min_date - timedelta(days=1)
    while current <= max_date:
        all_dates.append(current)
        current += timedelta(days=1)
    return all_dates

def make_y_list(dictionary, all_dates):
    sumtid = 0
    y = []
    for i in all_dates:
        i = i.isoformat()
        if i in dictionary:
            sumtid = dictionary[i]
        y.append(sumtid)
    return y

def main(data, dict_to_use, typ, filtrer=False, alfa=0.5):
    for thing_to_plot, farge in dict_to_use.items():
        if isinstance(thing_to_plot, (list, tuple)):
            nydata = sort_and_add_datetime(data, thing_to_plot, typ)
        else:
            nydata = sort_and_add_datetime(data, [thing_to_plot], typ)
        dictionary = dict()
        sumtid = 0
        date1 = None
        for i in nydata:
            if date1 == None:
                date1 = i['date']
            if date1 != i['date']:
                dictionary[date1] = sumtid
                date1 = i['date']
            sumtid += i['timeSpent'] / 60
        dictionary[date1] = sumtid

        dates = [date.fromisoformat(i) for i, _ in dictionary.items()]
        min_date = date(2025, 8, 5)
        max_date = min(datetime.now().date(), date(2025, 12, 24))

        all_dates = get_all_dates(min_date, max_date)

        # x = all_dates
        y = make_y_list(dictionary, all_dates)
        if filtrer:
            y = filterf.IIR(y, alfa)
        
        tittel = "Timer integrert over tid — "
        if isinstance(thing_to_plot, (list, tuple)):
            for i in range(len(thing_to_plot)):
                tittel += thing_to_plot[i]
                if i + 1 != len(thing_to_plot):
                    tittel += " + "
        else:
            tittel += thing_to_plot
        if filtrer:
            tittel += f" — IIR-filtrert m/ alfa = {alfa}"
        plott_x_y(all_dates, y, farge, tittel)

with open("logg.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

with open("fag_farger.json", "r", encoding="utf-8") as fil:
    farger = json.load(fil)

if filtrer:
    main(data, farger, "subject", True, alfa)
else:
    main(data, farger, "subject")

with open("type_farger.json", "r", encoding="utf-8") as fil:
    farger = json.load(fil)

if filtrer:
    main(data, farger, "type", True, alfa)
else:
    main(data, farger, "type")

farger = ot.main()

if filtrer:
    main(data, farger, "type", True, alfa)
else:
    main(data, farger, "type")


