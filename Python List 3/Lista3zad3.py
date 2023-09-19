#Kajetan Mieloch grupa 3 zadanie 3 z listy 3
from math import sqrt
a = int(input("Wprowadz liczbe a: "))
b = int(input("Wprowadz liczbe b: "))
c = int(input("Wprowadz liczbe c: "))

#Sprawdzamy czy równanie jest kwadratowe

delta = b*b - 4*a*c

if(delta >= 0):
    print("x1 = ", (-b-sqrt(delta))/(2*a))
    print("x2 = ", (-b+sqrt(delta))/(2*a))
else:
    print("Brak rozwiązań")
