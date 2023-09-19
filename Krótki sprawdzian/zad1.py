#Krótki sprawdzian zad1 Kajetan Mieloch grupa 3
def sumaListy(lista):
    suma = 0
    for e in range(len(lista)):
        if type(lista[e]) == int or type(lista[e]) == float:
            suma += lista[e]
        elif type(lista[e]) == list or type(lista[e]) == tuple:
            suma += sumaListy(lista[e])
    return suma


#program sumuje listy z samymi intami lub floatami
print(sumaListy([0.5,2,3,0.5]))
#program sumuje listy z intami i stringami pomijając stringi
print(sumaListy([1,2,3,'a','b']))
#program sumuje listy w liscie i tuple w liscie
print(sumaListy([[1,2,3], (1,2,3)]))
#program sumuje WSZYSTKIE liczby w liscie
#(włącznie z liczbami zagnieżdzonymi (lista w liscie, tupla w liscie)
#program uzywa do tego rekurencji
print(sumaListy([1,2,3,'a','b',1,2,3,'c','d', [1,2,3], (1,2,3)]))
print(sumaListy([[1,2],[3,0]]))
print(sumaListy([([1,2],[3,0],['a','b','c'],(1,2,[3]))]))

