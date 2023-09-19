#Kajetan Mieloch grupa 3 zadanie 1 z listy 6
import trojkat


a = int(input("podaj długość boku trójkątka a: "))
b = int(input("podaj długość boku trójkątka b: "))
c = int(input("podaj długość boku trójkątka c: "))

print(trojkat.obwodTroj(a,b,c))
print(trojkat.poleTroj(a,b,c))
print(trojkat.rodzajTroj(a,b,c))
print(trojkat.rodzajKata(a,b,c))

