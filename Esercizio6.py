'''
Lo pseudocodice seguente descrive come trasformare una stringa contenente un
numero telefonico a dieci cifre (come “4155551212”) in una stringa più facilmente
leggibile, formattata secondo lo stile statunitense, come “(415) 555–1212”.

• Prendere la stringa costituita dai primi tre caratteri e circondarla con
parentesi tonde (questo è il prefisso, detto “area code”).
• Concatenare il prefisso con la stringa contenente i tre caratteri successivi, un
trattino e la stringa costituita dagli ultimi quattro caratteri si ottiene il numero
nel formato richiesto

Tradurre questo pseudocodice in un programma Python che memorizzi un numero
telefonico di 10 cifre in una stringa, per poi visualizzarlo nel formato appena
descritto.
'''

number = input("Inserisci il numero telefonico: ")
if not(number.isdigit()):
    print(f"{number} non è un numero telefonico: contiene caratteri non numerici")
elif len(number) > 10:
    print(f"{number} non è un numero telefonico: troppo lungo")
elif len(number) < 10:
    print(f"{number} non è un numero telefonico: troppo corto")
else:
    print(f"Il numero telefonico è così formattato: ({number[0:3]}) {number[3:6]} {number[6:10]}")
