'''
Scrivere un programma che memorizzi in una costante un numero intero positivo di 
cinque cifre (quindi compreso tra 10000 e 99999), e visualizzi le singole cifre di cui 
è composto.  
Ad esempio, avendo il numero 16384, il programma deve visualizzare, su righe 
separate: 1 6 3 8 4.
'''

CONSTANT = input("Inserisci un numero intero positivo: ")

index = 0
while index < len(CONSTANT):
    if CONSTANT[index].isdigit():
        print(CONSTANT[index])
    index += 1
