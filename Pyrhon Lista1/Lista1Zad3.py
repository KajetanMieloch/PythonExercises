#Kajetan Mieloch

import math

bokA = input("podaj bok a: ")
bokB = input("podaj bok b: ")
katMiedzyBokami = input("podaj kat miedzy a i b: ")

def poleTrojkata(a,b,k):
    return 0.5*int(a)*int(b)*math.sin(math.radians(int(k)))

print(poleTrojkata(bokA, bokB, katMiedzyBokami))

#Odpowiedz: 4.388122209715023

