#Kajetan Mieloch

while True:
        a = input("podaj liczbe wiekrza: ")
        b = input("podaj liczbe mniejsza: ")

        a = int(a)
        b = int(b)
        if b<a:
                Z = (b/a)%1
                Z*=Z+3
                print(Z)
                break
        else:
                print("prosze podać 2 liczbe mniejsza niz 1")



