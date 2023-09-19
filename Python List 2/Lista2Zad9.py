#Kajetan Mieloch grupa 3 zad 9 z listy 2
from itertools import chain

lista = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

#używamy chain tak jak w domkumentacji
wynik = list(chain.from_iterable(lista))
 
print(wynik)
