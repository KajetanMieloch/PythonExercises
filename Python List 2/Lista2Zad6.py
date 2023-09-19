#Kajetan Mieloch grupa 3 zad 5 z listy 2

studenci = ["Kasia", "Basia", "Marek", "Darek"]
studenci.append("Józek")
studenci.extend(["Ania", "Basia"])
studenci.sort()
print(studenci[3])
print(studenci[0], studenci[1])
print(studenci[-2], studenci[-1])
#Póki basia jest na liście usuwaj basie
while "Basia" in studenci:
    studenci.remove("Basia")
print(len(studenci))
studenciTuple = tuple(studenci)
print(studenciTuple)
