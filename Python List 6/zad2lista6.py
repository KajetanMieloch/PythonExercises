#Kajetan Mieloch grupa 3 zadanie 2 z listy 6
import szyfrCezara

wybor = input("1- szyfrowanie, 2- deszyfrowanie: ")

if(wybor == 1):
    slowo = input("Podaj slowo do zakodowania: ")
    przes = int(input("Podaj ilość przesunięć podczas kodowania: "))

    print(szyfrCezara.szyfrowanie(slowo, przes))
else:
    slowo = input("Podaj slowo do rozkodowania: ")
    przes = int(input("Podaj ilość przesunięć podczas kodowania: "))

    print(szyfrCezara.deszyfrowanie(slowo, przes))





