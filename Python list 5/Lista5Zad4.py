def szyfrowanieIdeSzyfrowanie(tekst, tryb):
    #Wybieramy tryb szyfrowania(1) lub deszyfrowania (inne)
    if tryb == 0:
        #Definiujemy klucz
        klucz = {
            "a" : "y",
            "e" : "i",
            "i" : "o",
            "o" : "a",
            "y" : "e"
            }
        
        wynik = ""

        #dla litery w tekscie
        for l in tekst:
            #jeżeli jest w kluczu to dodajemy z klucza, jeżeli nie ma w kluczu przepisz
            try:
                wynik += klucz[l]
            except:
                wynik += l
                continue

        return wynik
    else:
        klucz = {
            "y" : "a",
            "i" : "e",
            "o" : "i",
            "a" : "o",
            "e" : "y"
            }
        
        wynik = ""
        
        for l in tekst:
            try:
                wynik += klucz[l]
            except:
                wynik += l
                continue

        return wynik

print(szyfrowanieIdeSzyfrowanie("to jest moj tekst", 0))
print(szyfrowanieIdeSzyfrowanie("ta jist maj tikst", 1))

print(szyfrowanieIdeSzyfrowanie("Przetestuj szyfrowanie i deszyfrowanie na kilku przykładach.", 0))
print(szyfrowanieIdeSzyfrowanie(szyfrowanieIdeSzyfrowanie("Przetestuj szyfrowanie i deszyfrowanie na kilku przykładach.", 0), 1))

print(szyfrowanieIdeSzyfrowanie("3 to wystarczająca ilośc przykładów", 0))
print(szyfrowanieIdeSzyfrowanie("3 ta westyrczyjący olaśc przekłydów", 1))

