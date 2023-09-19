#Kajetan Mieloch grupa 3 zadanie 1 z listy 4

lista = [1,1,2,3,5,8,13,21,34]
suma = 0
iloczyn = 1
#dla każdego elementu sumuj albo mnóż
for e in lista:
    suma += e
    iloczyn *= e

print("suma: ", suma)
print("iloczyn: ", iloczyn)
