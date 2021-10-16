'''
Scrivere un programma che memorizzi in due variabili costanti le lunghezze dei lati
di un rettangolo e visualizzi:
• L’area e il perimetro del rettangolo
• La lunghezza della sua diagonale
'''

import math

width = float(input("Inserisci la lunghezza di un lato: "))
height = float(input("Inserisci la lunghezza dell'altro lato: "))

print(f"Il perimetro del rettangolo è {width * 2 + height * 2}, l'area è {width * height}")
print(f"La diagonale corrisponde a {math.sqrt(width ** 2 + height ** 2)}")
