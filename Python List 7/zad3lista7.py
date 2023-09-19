#Kajetan Mieloch grupa 3 zadanie 3 z listy 7
import time
import random
from zad2lista7 import sortowanieWstawianie, generatorListy


def sortowanieBabelek(lista):
    st = time.time()
    n = len(lista)
    #używamy bardzo ciekawej opcji w pythonie, która pozwala nam na zamiane miejscami poszczególnych elementów w liście
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            #jeżeli nastepny element listy jest mniejszy to zamień miejscami elementy
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
                
        n -= 1
        if zamien == False:
            break

    et = time.time()
    czas = et - st
    print('Czas sortowania bombelkowo dla :',len(lista), "elementów", czas, "sekundy")
    return lista

print(sortowanieBabelek(generatorListy(100)))

l100 = generatorListy(100)
l200 = generatorListy(200)
l300 = generatorListy(300)
l400 = generatorListy(400)
l10000 = generatorListy(10000)

sortowanieWstawianie(l100)   
sortowanieBabelek(l100)
sortowanieWstawianie(l200)   
sortowanieBabelek(l200)
sortowanieWstawianie(l300)   
sortowanieBabelek(l300)
sortowanieWstawianie(l10000)   
sortowanieBabelek(l10000)

#Sortowanie przez wstawianie jest wolniejsze
