#Lista 9 grupa 3 zadanie 2
import numpy as np
import sys
dane = []
try:
    #Wczytywanie z konsoli 
    sys.argv[1]
    for ile, wart in enumerate(sys.argv):
        #Odrzucamy argument 0, ponieważ jest to nazwa pliku
        if ile == 0:
            continue
        dane.append(float(wart))
except:
   #Wczytywanie z pliku
   for i in input().split():
        #Musimy sprawdzic czy w pliku sa same liczby czy tez mamy do czynienia z białymi
        #znakami lub stringami 
        try:
            dane.append(float(i))
        except:
            continue
            



print("Średnia wynosi:",np.mean(dane))
print("Wariancja:",np.var(dane))
print("Odchylenie standardowe:",np.std(dane))

