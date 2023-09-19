#Kajetan Mieloch grupa 3 zad 5 z listy 2
napis = input("Wprowadz napis: ")

#Dowiadujemy się o długości napisu
srodekIndxNONINT = len(napis)/2

#Konwertujemy długość napisu na int
srodekIndx = int(srodekIndxNONINT)

#Wstawiamy napis python w środek innego napisu
print(napis[:srodekIndx] + 'Python' + napis[srodekIndx:])
