#Kajetan Mieloch grupa 3 zad 10 z listy 2
lista = []
licz = 0
liczAfter5 = 0

#Korzystając z range tworzymy listę zawierającą wielokrotoności liczby 3 mniejsze od 100
for n in range(3, 100, 3):
    lista.append(n)

#dla każdej liczby w liście
for n in lista:
    #jeżeli 5 element listy
    if(licz >= 4):
        #uruchom liczenie co 3 liczby
        if(liczAfter5 % 2 == 0):
            #usun co 3 liczbe zaczynając od 5 elementu
            del lista[licz]
        liczAfter5 += 1     
    
    licz += 1

#podziel sume listy przez długość listy
wynik = sum(lista)/len(lista)

print(wynik)
