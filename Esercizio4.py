count = int(input("Inserisci il numero di libri: "))
total = float(input("Inserisci il costo totale dei libri: "))

tax = round(total * 0.075)
expedition = round(count * 2)

print(f"Il costo totale è {total + tax + expedition} di cui {tax} sono tasse e {expedition} sono spese di spedizione")