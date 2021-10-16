'''
Scrivere un programma che memorizzi due numeri interi in due costanti definite nel 
codice, e poi ne visualizzi: 
• La somma 
• La differenza 
• Il prodotto 
• Il valore medio 
• La distanza (cioè il valore assoluto della differenza) 
• Il valore massimo (cioè il maggiore tra i due) 
• Il valore minimo (cioè il minore tra i due) 
 
Suggerimento: utilizzare le funzioni max e min definite in Python. Esse accettano 
una sequenza di valori separati da virgola in input e restituiscono rispettivamente il 
valore massimo e minimo della sequenza. (Es: max(10, 5) restituisce 10).
'''

import math

CONSTANT1 = math.e
CONSTANT2 = math.pi

print(f"{CONSTANT1=} {CONSTANT2=}\n")

print(f"La somma è {CONSTANT1 + CONSTANT2}")
print(f"La differenza è {CONSTANT1 - CONSTANT2}")
print(f"Il prodotto è {CONSTANT1 * CONSTANT2}")
print(f"Il valore medio è {(CONSTANT1 + CONSTANT2) / 2}")
print(f"La distanza è {abs(CONSTANT1 - CONSTANT2)}")
print(f"Il valore massimo è {max(CONSTANT1,CONSTANT2)}")
print(f"Il valore minimo è {min(CONSTANT1,CONSTANT2)}")
