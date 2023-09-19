#Kajetan Mieloch grupa 3 zadanie 7 z listy 4

def wypiszPascala(wierszy):
    #nowa lista
    lista = [];
    #jeżeli jeszcze są wiersze
    while (wierszy > 0):
        #dodajemy do siebie liczby z listy według algorytmu.
        for i in range(1, len(lista)):
            lista[i] = lista[i] + lista[i - 1]
        lista.append(1)
        txt = "";
        for x in range(0, int(wierszy/2)):
            txt += "\t"
        #dodajemy tabulatory
        for a in enumerate(lista):
            if (wierszy % 2 == 1):
                txt += "  "
            txt += str(a[1]) + "\t"
        print(txt)
        #odejmujemy wiersz, pętla wraca do ponownego działania.
        wierszy = wierszy - 1

n = int(input("Podaj liczbę wierszy: "));
wypiszPascala(n);
