#Kajetan Mieloch grupa 3 zadanie 9 z listy 3
m = int(input("Podaj ilość wierszy: "))
n = int(input("Podaj ilość kolumn: "))

#Graficzna reprezentacja
for w in range(m):
    for k in range(n):
        #podwójna pętla, printowanie w jednej kolumnie
        print((w+1)*(k+1),end=' ')
    #nowa linia
    print('\t')

wiersz = []
wynik = []

#Lista 2D
for w in range(m):
    #Usuwamy wartości z poprzedniego wierszu
    wiersz.clear()
    for k in range(n):
        #dodajemy pokolei wartości do zmiennej wiersz
        wiersz.append((w+1)*(k+1))
    #Wynik kopiuje tablice wiersz NALEŻY UŻYĆ LIST ABY NIE UŻYWAĆ REFERENCJI A FAKTYCZNYCH WARTOŚCI
    wynik.insert(w,list(wiersz))

print(wynik)
