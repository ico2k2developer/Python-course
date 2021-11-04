"""
Scrivete programmi che leggano una riga di dati in ingresso sotto forma di stringa e 
visualizzino quanto segue: 
a. le sole lettere maiuscole della stringa; 
b. a partire dalla seconda lettera della stringa, una lettera viene visualizzata e 
l’altra no, alternativamente; 
c. la stringa con tutte le vocali sostituita da un carattere di sottolineatura 
(underscore); 
d. il numero di cifre presenti nella stringa; 
e. le posizioni di tutte le vocali presenti nella stringa.
"""

REPLACE = "_"

data = input("Inserire una stringa: ")
upper = ""
alpha = ""
replaced = ""
pos = ""
alphaCount = 0
digitCount = 0
index = 0
last = 0
for ch in data:
    if ch.isupper():
        upper += ch
    if ch.isalpha():
        if alphaCount > 0:
            if alphaCount % 2 != 0:
                alpha += ch
        if ch.lower() in "aieou":
            if index > 0:
                replaced += data[last + 1:index]
            replaced += REPLACE
            pos += f"{index + 1} "
            last = index
        alphaCount += 1
    if ch.isdigit():
        digitCount += 1
    index += 1
print(f"Le sole lettere maiuscole della stringa: {upper}")
print(f"Una lettera sì e una no, a partire dalla seconda: {alpha}")
print(f"La stringa con le vocali sostituite da {REPLACE}: {replaced}")
print(f"Nella stringa sono presenti {digitCount} cifre")
print(f"Le vocali nella stringa si trovano nelle posizioni: {pos}")
