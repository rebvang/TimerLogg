import matplotlib.pyplot as plt


def do_int(liste):
    return [int(i) for i in liste]

def finn_tid(objekt):
    start_t, start_m = do_int(objekt['start'].split(":"))
    slutt_t, slutt_m = do_int(objekt['end'].split(":"))
    retur = dict()
    if start_t == slutt_t:
        tid = slutt_m - start_m
        time = start_t
        retur[time] = tid
        return retur
    if slutt_t > start_t:
        retur[start_t] = 60 - start_m
        for i in range(start_t + 1, slutt_t):
            retur[i] = 60
        retur[slutt_t] = slutt_m
        return retur
    if start_t > slutt_t:
        raise ValueError

def lag_plott(data, typ=False, farge=False):
    tid = dict()
    for i in range(4, 24):
        tid[i] = 0

    for n in data:
        timer = finn_tid(n)
        for i, m in timer.items():
            tid[i] += m

    x, y = zip(*tid.items())
    y = [i/60 for i in y]


    plt.figure(figsize=(8, 5))
    if typ:
        plt.title(f"Tid brukt per time — {typ}")
    else:
        plt.title(f"Stolpediagram av total tid brukt for hver time i løpet av en dag")
    plt.xticks([i for i in range(4, 24)])
    plt.ylabel("Timer")
    plt.xlabel("Klokkeslett")
    plt.grid(axis='y', alpha=0.3)

    if not farge or farge == "":
        plt.bar(x, y)
    else:
        plt.bar(x, y, color=farge)
    if typ:
        plt.savefig(f"../plots/{typ}.png")
    plt.show()