#Kajetan Mieloch grupa 3 zadanie 2 z listy 6

def popaSeISeNapisz(n, poczWart = 1):

    #Działa tylko dla cyfr
    if poczWart > 9:
        return "Początkowa wartość musi być mniejsza niż 10"

    #ustalamy początkowe wartości
    poczWart = str(poczWart)
    if (n == 1):
        return poczWart
    if (n == 2):
        return "1"+poczWart
    podst = "1"+poczWart
    #używamy znaku| żeby rozdzielić kolejne liczby ciągu
    for i in range(3, n + 1):
        podst += '|'
        l = len(podst)
        tempNumb = 1
        tmp = ""
        #sprawdzamy czy stojące obok liczby są torżsame
        for j in range(1 , l):
            if (podst[j] != podst[j - 1]):
                tmp += str(tempNumb + 0)
                tmp += podst[j - 1]
                tempNumb = 1
            else:
                tempNumb += 1
        podst = tmp
    return podst;

n = 5
print(popaSeISeNapisz(n, 7))
