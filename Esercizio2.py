CONSTANT = input("Inserisci un numero intero positivo: ")

index = 0
while index < len(CONSTANT):
    if CONSTANT[index].isdigit():
        print(CONSTANT[index])
    index += 1