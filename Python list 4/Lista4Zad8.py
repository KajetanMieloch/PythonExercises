#Kajetan Mieloch grupa 3 zadanie 8 z listy 4

#Rekurencyjne rozwiązanie
def sum(n):
    #n mniejsze niż 2, na pewno 1
    if n < 2:
        return 1
 
    else:
        #inaczej rekurencja z n mniejszym o 1
        return 1 / n + (sum(n - 1))

print(sum(2))
print(sum(8))
print(sum(10))
print(sum(15))
