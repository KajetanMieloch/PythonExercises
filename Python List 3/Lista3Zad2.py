#Kajetan Mieloch grupa 3 zadanie 2 z listy 3
import sys
liczba = int(input("Wpisz liczbe: "))

#wersja z if:
if(liczba%2 == 0):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

#wersja bez if:

#Jeżeli liczba będzie nieparzysta to while się wykona ponieważ 1 = True.
#Wypisze liczba nieparzysta nastepnie program się zakończy.
#Jeżeli liczba będzie parzysta to while zostanie zupełnie pominięty.
while liczba%2:
    print("Liczba nieparzysta")
    sys.exit()

print("Liczba parzysta")


