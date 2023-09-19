#Kajetan Mieloch grupa 3 zadanie 5 z listy 3
from re import fullmatch

#Zasady które hasło musi spełaniać
zasady = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[$#@]).{6,16}$"
haslo = input("Wpisz hasło: ")
#Używamy metody z biblioteki re, aby sprawdzić czy hasło wpasowuje się w zasady
wynik = fullmatch(zasady, haslo)

if wynik:
  print("Hasło spełnia wymagania")
else:
  print("Hasło nie spełnia wymagań")	
