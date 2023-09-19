#Kajetan Mieloch
napis = input("Wprowadz napis: ")
pierwszyZnak = napis[0]
napisMod = napis[1:]

napisZmienione = napisMod.replace(pierwszyZnak, '$')

wynik = pierwszyZnak + napisZmienione

print(wynik)
