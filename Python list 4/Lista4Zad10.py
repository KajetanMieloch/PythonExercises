#Kajetan Mieloch grupa 3 zadanie 10 z listy 4

#używamy algorytm Euklidesa
def gcdExtended(a, b):
 
    #podstawowy warunek
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    #Przypisujemy nowe X i Y
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y
 

a, b = 121, 21
g, x, y = gcdExtended(a, b)
print("NWD(", a, ",", b, ") = ", g)
