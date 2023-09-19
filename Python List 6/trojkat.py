#Moduł do zadania 1 z listy 6
import math

#Sprawdzamy czy podany trójkąt instnieje

def czyIst(a,b,c):
    liczby = [a,b,c]
    liczby.sort()
    minD = liczby[0]
    middleD = liczby[1]
    maxD = liczby[2]

    #Najdłuzszy bok musi być więkrzy od sumy pozostałych boków
    if(maxD < middleD + minD):
        return 0
    return 1

def obwodTroj(a,b,c):
    if(czyIst(a,b,c)):
        return "Podany trojkąt nie istnieje! Spróbuj ponownie"
    
    return a+b+c

def poleTroj(a,b,c):
    if(czyIst(a,b,c)):
        return "Podany trojkąt nie istnieje! Spróbuj ponownie"
    
    p  = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def rodzajTroj(a,b,c):
    if(czyIst(a,b,c)):
        return "Podany trojkąt nie istnieje! Spróbuj ponownie"

    if(a==b==c):
        return "równoboczny"
    if(a==b) or (a==c) or (b==c):
        return "równoramienny"
    return "różnoboczny"

def rodzajKata(a,b,c):
    if(czyIst(a,b,c)):
        return "Podany trojkąt nie istnieje! Spróbuj ponownie"
    
    liczby = [a,b,c]
    liczby.sort()
    minD = liczby[0]
    middleD = liczby[1]
    maxD = liczby[2]

    if(maxD**2==middleD**2+minD**2):
        return "prostokątny"
    if(maxD**2<middleD**2+minD**2):
        return "ostrokątny"
    if(maxD**2>middleD**2+minD**2):
        return "rozwartokątny"
