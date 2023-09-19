#Kajetan Mieloch grupa 3 zadanie 6 z listy 4
import math

#należy użyć algorytmu na konwersje
def RGBtoHSV(r,g,b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
 
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax-cmin
 
    if cmax == cmin:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
    v = cmax * 100
    return h, s, v

#Przykładowe konwersje
print(RGBtoHSV(10,20,50))
print(RGBtoHSV(5,40,30))
print(RGBtoHSV(100,200,40))
