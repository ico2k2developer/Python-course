"""
Scrivete la funzione:
def countWords(string)

che restituisca il numero di parole presenti nella stringa string. Le parole sono
sequenze di caratteri separate da spazi (si ipotizzi che tra due parole consecutive vi
sia esattamente uno spazio). Ad esempio, countWords("Mary had a little
lamb") restituisce 5.
Come si potrebbe estendere l’esercizio in modo da trattare correttamente delle
stringhe in cui siano presenti più spazi tra le parole?
"""


def main():
    t = input("Inserisci del testo: ")
    print(f"Il testo ha {countwords(t)} parole")


def countwords(word):
    count = 0
    valid = True
    for a in word:
        if a in " ":
            valid = True
        elif a.isalpha():
            if valid:
                count += 1
                valid = False
    return count


main()
