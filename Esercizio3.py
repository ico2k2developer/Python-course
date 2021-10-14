string = input("Inserisci una stringa: ")

if len(string) >= 6:
    print(f"{string[0:3]}...{string[len(string) - 3:len(string)]}")
else:
    print("Stringa troppo corta!")