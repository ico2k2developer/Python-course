"""
Scrivete programmi che leggano una sequenza di numeri interi (la sequenza termina 
quando viene inserita la stringa vuota) che visualizzino quanto segue: 
a. il valore minimo e il valore massimo tra quelli acquisiti 
b. il numero di valori pari e il numero di valori dispari tra quelli acquisiti; 
c. le somme parziali di tutti i numeri acquisiti, calcolate e visualizzate dopo ogni 
nuova acquisizione (se, ad esempio, i valori in ingresso sono 1 7 2 9, il 
programma visualizzerà 1 8 10 19); 
d. i valori adiacenti duplicati (se, ad esempio, i valori acquisiti sono 1 3 3 4 5 5 6 
6 6 3, il programma visualizzerà 3 5 6).
"""

n = input("Inserisci un numero intero: ")
maxValue = ""
minValue = ""
even = 0
odd = 0
sum = 0
count = 0
doubles = ""
last = ""
while n != "":
    if n.isdigit():
        n = int(n)
        if isinstance(maxValue, int):
            if maxValue < n:
                maxValue = n
        else:
            maxValue = n
        if isinstance(minValue, int):
            if minValue > n:
                minValue = n
        else:
            minValue = n
        if isinstance(last, int):
            if last == n and not (str(last) in doubles):
                doubles += f"{last} "
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        sum += n
        count += 1
        last = n
        print(f"La somma parziale è {sum}")
    else:
        print(f"{n} non è un numero intero")
    n = input("Inserisci un altro numero intero: ")
print(f"Sono stati inseriti {count} valori di cui {even} pari e {odd} dispari")
print(f"Il valore minimo è {minValue}, il valore massimo è {maxValue}")
print(f"I valori adiacenti duplicati sono {doubles}")
