#Kajetan Mieloch grupa 3 zadanie 2 z listy 8
import szyfrCezara
from datetime import date
import os

nazwaFolderu = input("Podaj nazwe folderu: ")

#Tu skończone

with open(sciezka, 'r') as f:
    slowo = f.read()
    przes = int(input("Podaj ilość przesunięć podczas kodowania (1-10): "))
    f.close()

if przes in range(1,11):
    nazwaFolderu = input("Podaj nazwe folderu: ")
    if os.path.isdir(nazwaFolderu) == False:
        os.mkdir(nazwaFolderu)
    nazwaPliku = 'plik_zaszyfrowany'+str(przes)+"_"+date.today().strftime("%Y%m%d")+".txt"

    sciezkaINazwa = os.path.join(nazwaFolderu, nazwaPliku)


    with open(sciezkaINazwa, 'w+') as f:
        f.write(szyfrCezara.szyfrowanie(slowo, przes))
        f.close()
else:
    print('Należy podać liczbe z zakresu 1-10!')


