#Kajetan Mieloch grupa 3 zadanie 7 z listy 3


def Fibonacci(first, second, length):

    #jeżeli dlugosc = 0 to koniec
    if(length == 0):
        return

    #wypisuje numer z ciągu
    print(first + second, end=" ")

    #Rekurencja
    Fibonacci(second, first+second, length-1)



n = int(input("Ile elementów ciągu ci wypisać?: ")) - 2

if n < 0:
    print("Podaj liczbę wiekrzą niż 2")
else: 
    #zawsze na początku będzie 0 i 1.
    print(0,1,end=" ")
    Fibonacci(0,1,n)
