#Kajetan Mieloch grupa 3 zadanie 1 z listy 7
import time


def FibFor(n):
    st = time.time()
    #podstawowe założenia
    wynik = "0"
    if n == 0:
        wynik = "0"
        return wynik
    if n == 1:
        wynik = "0,1"
        return wynik
    if n == 2:
        wynik = "0,1,1"
        return wynik
    n-=2
    wynik = "0,1,1"
    pop1 = 1
    pop2 = 1
    nast = 0
    zam = 0
    for i in range(n):
        zam += 1
        nast = pop1 + pop2
        if zam%2 == 0:
            pop1 = nast
        else:
            pop2 = nast
        wynik += ","
        wynik += str(nast)
        et = time.time()
    czas = et - st
    print('Czas wykonywania programu wersja FOR:', czas, "sekundy")
    return wynik

def FibRek(n):
    if n <=1:
        return n
    else:
        return FibRek(n-1) + FibRek(n-2)

def FibRekPrint(n):
    #Funkcja do printowania sekwencji
    st = time.time()
    wynik = ""
    n += 1
    for i in range(n):
        wynik += str(FibRek(i))
        wynik += ","
    et = time.time()
    czas = et - st
    print('Czas wykonywania programu wersja Rekurencyjna:', czas, "sekund")
    return wynik

ilosc_wyk = 35

#Wersja rekurencyjna jest o wiele wiele wolniejsza

print(FibRekPrint(ilosc_wyk))
print(FibFor(ilosc_wyk))

