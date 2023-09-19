#Moduł do zadania 2 z listy 6

dozwZnaki = []
for l in range(65, 91):
    dozwZnaki.append(l)
for l in range(97, 122):
    dozwZnaki.append(l)
for l in range(260, 264):
    dozwZnaki.append(l)
for l in range(280, 282):
    dozwZnaki.append(l)
for l in range(321, 325):
    dozwZnaki.append(l)
for l in range(377, 381):
    dozwZnaki.append(l)
dozwZnaki.append(243)
dozwZnaki.append(211)
dozwZnaki.append(346)
dozwZnaki.append(347)

def szyfrowanie(slowo, ilePrzesun):
    #definiujemy liste z wszystkimi dozwolonymi znakami

    nowSlowo = []
    poprawPrzes = ilePrzesun

    #upewniamy się, że przesunięcie będzie za duże, więc redukujemy ilość przesunięć.
    while poprawPrzes > len(dozwZnaki):
        poprawPrzes -= len(dozwZnaki)

    #sprawdzamy czy litera ze slowa jest w dozwolonych znakach, jeśli tak to ją zamień według klucza. Jeśli przekroczy zakres id szyfr zapętla się
    for l in slowo:
        asciL = ord(l)
        if(asciL in dozwZnaki):
            if(dozwZnaki.index(asciL) + poprawPrzes >= len(dozwZnaki)):
                nowSlowo.append(chr(dozwZnaki[dozwZnaki.index(asciL)+poprawPrzes - len(dozwZnaki)]))
            else:
                nowSlowo.append(chr(dozwZnaki[dozwZnaki.index(asciL)+poprawPrzes]))
        else:
            nowSlowo.append(l)

    return ''.join(nowSlowo)

#W deszyfrowaniu zamieniłem 1 minus na plus i 3 plusy na minusy.
def deszyfrowanie(slowo, ilePrzesun):
    nowSlowo = []
    poprawPrzes = ilePrzesun

    while poprawPrzes > len(dozwZnaki):
        poprawPrzes -= len(dozwZnaki)

    for l in slowo:
        asciL = ord(l)
        if(asciL in dozwZnaki):
            if(dozwZnaki.index(asciL) - poprawPrzes >= len(dozwZnaki)):
                nowSlowo.append(chr(dozwZnaki[dozwZnaki.index(asciL)-poprawPrzes + len(dozwZnaki)]))
            else:
                nowSlowo.append(chr(dozwZnaki[dozwZnaki.index(asciL)-poprawPrzes]))
        else:
            nowSlowo.append(l)

    return ''.join(nowSlowo)
