"""
Scrivete la funzione merge(a, b) che “fonde” due liste, alternando un elemento 
della prima e un elemento della seconda. Se una lista è più corta dell’altra, gli 
elementi vengono alternati fin quando è possibile, poi gli elementi rimasti nella lista 
più lunga vengono aggiunti ordinatamente in fondo. Le liste di partenza non devono 
essere modificate. Se, ad esempio, il contenuto di a è 1 4 9 16 e il contenuto di b è 
9 7 4 9 11, l’invocazione di merge(a, b) restituisce una nuova lista contenente i 
valori 1 9 4 7 9 4 16 9 11.
"""

def main():
    a = (1, 4, 9, 16)
    b = (9, 7, 4, 9, 11)
    print(f"Lista a: {a}")
    print(f"Lista b: {b}")
    c = merge(a, b)
    print(f"Lista risultante: {c}")


def merge(list1, list2):
    result = []
    smaller = list1
    bigger = list2
    if len(bigger) < len(smaller):
        smaller = list2
        bigger = list1
    for i in range(len(smaller)):
        result.append(list1[i])
        result.append(list2[i])

    for i in range(len(smaller), len(bigger)):
        result.append(bigger[i])

    return result


main()
