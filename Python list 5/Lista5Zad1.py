#Kajetan Mieloch grupa 3 zadanie 1 z listy 5

def zmianaSlowNaDzies(liczbaStr):
    #definiujemy słownik
    liczby = {
        "jeden" : 1,
        "dwa" : 2,
        "trzy" : 3,
        "cztery" : 4,
        "pięć" : 5,
        "sześć" : 6,
        "siedem" : 7,
        "osiem" : 8,
        "dziewięć" : 9,
        "dziesięć" : 10,
        "jedenaście" : 11,
        "dwanaście" : 12,
        "trzynaście" : 13,
        "czternaście" : 14,
        "piętnaście" : 15,
        "szesnaście" : 16,
        "siedemnaście" : 17,
        "osiemnaście" : 18,
        "dziewiętnaście" : 19,
        "dwadzieścia" : 20,
        "trzydzieści" : 30,
        "czterdzieści" : 40,
        "pięćdziesiąt" : 50,        
    }

    wynik = 0

    #uzywamy try, ponieważ częste są literówki od usera
    try:
        #splitujemy i dla każdego elementu sprawdzamy pozycje w słowniku.
        strSplited = liczbaStr.split()
        for i in strSplited:
            #i.lower, aby różnice w wielkości liter nie wywalały błędu
            wynik += int(liczby[i.lower()])

        
    except:
        print("Upewnij się, że użyłeś polskich znaków. Pamietaj o porawnej pisowni!")

    return wynik


liczbaStr = input("podaj słownie liczbę od 1 do 59: ")

print(zmianaSlowNaDzies(liczbaStr))
