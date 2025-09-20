def FIR(liste, M):
    returliste = []
    for i in range(len(liste)):
        if i < M - 1:
            verdi = sum(liste[:i+1])/len(liste[:i+1])
            returliste.append(verdi)
            continue
        verdi = sum(liste[i-M+1:i+1])/len(liste[i-M+1:i+1])
        returliste.append(verdi)
    return returliste

def IIR(liste, alfa):
    returliste = [liste[0]]
    for i in liste[1:]:
        verdi = returliste[-1] * alfa + i * (1 - alfa)
        returliste.append(verdi)
    return returliste