#Kajetan Mieloch grupa 3 zadanie 3 z listy 4
import math

def liczStoplubRad(tryb, wejscie):
    #proste menu. Przy uzyciu biblioteki math liczymy odpowiednio stopnie, lub radiany
    print("wynik wynosi: ")
    if(tryb == 1):
        print(math.radians(wejscie), "radianów")
    elif(tryb == 2):
        print(math.degrees(wejscie), "stopni")
    else:
        print("Podaj poprawny tryb")


print("1 - stopnie na radiany")
print("2 - radiany na stopnie")
tryb = int(input("podaj tryb: "))
wejscie = int(input("podaj liczbe: "))

liczStoplubRad(tryb, wejscie)
