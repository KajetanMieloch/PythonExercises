#Kajetan Mieloch grupa 3 zadanie 5 z listy 4
from itertools import permutations 

def permutacje(lista):
    perm = permutations(lista) 
    for i in list(perm):
        print (i)

permutacje([1,2,3])
permutacje([1,2,3,4])
permutacje([1,2,3,4,5])

