#Kajetan Mieloch grupa 3 zadanie 9 z listy 4

#silnia n, bez rekurencji
n=int(input("Wpisz liczbę:"))
f=1
#jeżeli n wiekrze niż 0, pętla działą
while(n>0):
    #f = f razy n które jest za każdym razem mniejsze o 1
    f=f*n
    n=n-1
print("Wynik dla silni z", n ,"jest: ")
print(fact)
