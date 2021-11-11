"""
Un’organizzazione non governativa ha bisogno di un programma per calcolare la
quota di sussidio economico da assegnare a ciascuna famiglia bisognosa di
assistenza. La formula è la seguente:
• Se il reddito annuo della famiglia è compreso tra $ 30 000 e $ 40 000 e la
famiglia ha almeno tre figli, il sussidio è pari a $ 1000 per ogni figlio.
• Se il reddito annuo della famiglia è compreso tra $ 20 000 e $ 30 000 e la
famiglia ha almeno due figli, il sussidio è pari a $ 1500 per ogni figlio.
• Se il reddito annuo della famiglia è minore di $ 20 000, il sussidio è pari a $
2000 per ogni figlio.

Scrivete una funzione che faccia questi calcoli, poi scrivete un programma che in un
ciclo chieda all’utente di fornire il reddito annuo e il numero di figli di ciascuna
famiglia richiedente il sussidio, visualizzando il valore corrispondentemente
restituito dalla funzione. Usate –1 come valore sentinella per terminare l’immissione
dei dati.
"""


def main():
    while True:
        i = input("Inserisci il reddito annuo: ")
        r = value(i)
        while r < 0:
            if i == "-1":
                return
            i = input("Inserisci il reddito annuo correttamente: ")
            r = value(i)
        i = input("Inserisci il numero di figli: ")
        s = value(i)
        while s < 0:
            if i == "-1":
                return
            i = input("Inserisci il numero di figli correttamente: ")
            s = value(i)
        print(f"Il sussidio economico assegnato è {subside(r, s)}")


def value(text):
    if text.isdigit():
        return int(text)
    else:
        return -2


def subside(wealth, sons):
    result = 0
    if wealth <= 40000:
        if wealth > 30000:
            if sons > 2:
                result = 1000 * sons
        elif wealth > 20000:
            if sons > 1:
                result = 1500 * sons
        else:
            result = 2000 * sons
    return result


main()
