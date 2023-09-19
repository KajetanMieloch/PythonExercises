#Kajetan Mieloch grupa 3 zad 7 z listy 2

lista = [(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
listaRev = []
wynik = []

#dla każej tupli w liscie
for t in lista:
    #odwróć tuple
    tupleRev = reversed(t)
    tupleRev = tuple(tupleRev)
    #tworzymy nową liste
    listaRev.append(tupleRev)

#sortujemy nową liste
listaRev.sort()

#dla każej tupli w nowej liscie
for t in listaRev:
    #odwróć tuple
    tupleRev = reversed(t)
    tupleRev = tuple(tupleRev)
    #tworzymy nową liste
    wynik.append(tupleRev)

print(wynik)


