"""
Scrivete un programma che inizializzi una lista con dieci numeri interi casuali tra 1 e
100 e, poi, visualizzi quattro righe di informazioni, contenenti:
a. Tutti gli elementi di indice pari.
b. Tutti gli elementi di valore pari.
c. Tutti gli elementi in ordine inverso.
d. Il primo e l’ultimo elemento.
"""
import random


def main():
    l = [0] * 10
    for i in range(len(l)):
        l[i] = random.randint(1, 100)

    print("I numeri di indice pari sono:")
    for i in range(len(l)):
        if i % 2 == 0:
            print(str(l[i]), end=" ")

    print("\nI numeri di valore pari sono:")
    for i in range(len(l)):
        if l[i] % 2 == 0:
            print(str(l[i]), end=" ")

    print("\nI numeri in ordine inverso:")
    for i in range(len(l)):
        print(l[len(l) - 1 - i], end=" ")

    print(f"\nIl primo elemento è {l[0]} e l'ultimo è {l[len(l) - 1]}")


main()
