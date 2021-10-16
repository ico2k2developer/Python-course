'''
Scrivere un programma che memorizzi una stringa in una variabile e, a partire da 
quella variabile, visualizzi i primi tre caratteri della stringa, seguiti da tre punti, 
ancora seguiti dagli ultimi tre caratteri. 
Ad esempio, se la stringa viene inizializzata al valore “Mississippi”, il programma 
deve visualizzare “Mis...ppi”. [P2.22] 
Cosa succede della stringa è più corta di 6 caratteri? E se è più breve di 3 caratteri?
'''

string = input("Inserisci una stringa: ")

if len(string) >= 6:
    print(f"{string[0:3]}...{string[len(string) - 3:len(string)]}")
else:
    print("Stringa troppo corta!")
