#Kajetan Mieloch grupa 3 zadanie 4 z listy 4

#definiujemy standardowe wejscia funkcji
def liczCiag(n, a1=1, q=2):
    an = a1*q**(n-1)
    #zwracamy wynik
    return an

#wywołanie funkcji
print(liczCiag(7,3,2))
print(liczCiag(7,3))
print(liczCiag(2))

