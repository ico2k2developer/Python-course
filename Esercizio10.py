"""
Scrivete la funzione:
def countVowels(string)

che restituisca il numero di vocali presenti nella stringa string. Le vocali sono le
lettere a, e, i, o e u, oltre alle rispettive versioni maiuscole.
"""


def main():
    t = input("Inserisci una parola: ")
    print(f"La parola ha {countvowels(t)} vocali")


def countvowels(word):
    count = 0
    for a in word:
        if a.lower() in "aieouáàéèíìóòúù":
            count += 1
    return count


main()
