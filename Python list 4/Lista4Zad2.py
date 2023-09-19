#Kajetan Mieloch grupa 3 zadanie 2 z listy 4

#definiujemy funkcje
def usunPow(lista):
    duplikaty = []
    #dla każdego elementu sprawdzamy czy jest w duplikatach,
    #jeżeli tak to nic się nie dzieje
    #jeżeli nie ma go w liście duplikaty dodaj go do listy duplikaty.
    for e in lista:
        if e in duplikaty:
            pass
        else:
            duplikaty.append(e)

    print(duplikaty)

usunPow([1,1,1,2,3,3,7,1,2,3,1])
