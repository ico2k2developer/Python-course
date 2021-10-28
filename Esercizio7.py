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
