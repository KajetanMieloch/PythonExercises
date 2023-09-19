#Kajetan Mieloch
import cmath

x = input("podaj liczbe zespolona (np. 1.123+1.123j)")
x = complex(x)
print(x)
print(abs(x))
print(cmath.phase(x))
print(x.conjugate())
