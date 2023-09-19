#Kajetan Mieloch grupa 3 zadanie 8 z listy 3

def liczby(i):
    #Tylko do 9
    if i == 10:
        pass
    #rekurencyjnie wypisuje liczby o 1 więcej
    else:
        print(str(i)*i)
        return liczby(i+1)    


liczby(1)
