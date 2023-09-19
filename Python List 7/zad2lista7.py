#Kajetan Mieloch grupa 3 zadanie 1 z listy 7
import time
import random

def sortowanieWstawianie(lista):
    st = time.time()
    for i in range(1,len(lista)):
        #zaczynamy od 1
        temp=lista[i]
        j=i-1
        #j jest wskaznikiem do aktualnej pozycji liczby przesuwanej
        while j>=0 and lista[j]>temp:
            #przy każdym powtórzeniu petli odejmujemy j,
            #póki jest ono wiekrze bądź równe 0 kontynułujemy pętlę,
            #no chyba że startowa liczba jest wiekrza
            lista[j+1]=lista[j]
            j-=1
            lista[j+1]=temp
    et = time.time()
    czas = et-st
    print('Czas sortowania przez wstawianie dla :',len(lista), "elementów", czas, "sekundy")
    return lista

#generujemy liste z przedziału <0,20>
def generatorListy(ile):
    lista = []
    for i in range(ile):
         lista.append(random.randint(0, 20))   

    return lista

if __name__ == "__main__":
    print(sortowanieWstawianie(generatorListy(100)))
    print(sortowanieWstawianie(generatorListy(200)))
    print(sortowanieWstawianie(generatorListy(300)))
