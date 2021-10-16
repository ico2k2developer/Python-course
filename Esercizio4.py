'''
Lo pseudocodice seguente descrive come, in una libreria, viene calcolato l’importo di 
un ordine a partire dal costo totale dei libri ordinati e dal loro numero.  
 
• Leggere il costo totale dei libri e il numero di libri. 
• Calcolare le tasse (il 7.5 per cento del costo totale dei libri). 
• Calcolare i costi di spedizione ($2 per ogni libro). 
• Il prezzo totale dell’ordine è la somma del costo totale dei libri, delle tasse e 
dei costi di spedizione. 
• Visualizzare l’importo dell’ordine. 
 
Scrivere un programma in Python che implementi questo pseudocodice. Il costo 
totale dei libri e il numero di libri devono essere memorizzati in due variabili 
costanti.
'''

count = int(input("Inserisci il numero di libri: "))
total = float(input("Inserisci il costo totale dei libri: "))

tax = round(total * 0.075)
expedition = round(count * 2)

print(f"Il costo totale è {total + tax + expedition} di cui {tax} sono tasse e {expedition} sono spese di spedizione")
