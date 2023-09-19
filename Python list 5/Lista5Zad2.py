#Kajetan Mieloch grupa 3 zadanie 2 z listy 5

def zmienLiczbeNaStr(liczba):
    l = len(liczba)
  
    if (l == 0):
        print("dlugosc 0")
        return
  
    if (l > 4):
        print("za duza liczba")
        return
  
    cyfra = ["zero", "jeden", "dwa", "trzy",
                     "cztery", "pięć", "sześć", "siedem",
                     "osiem", "dziewięć"]
  
    nascie = ["dziesięć", "jedenaście", "dwanaście",
                  "trzynaście", "czternaście", "piętnaście",
                  "szesnaście", "siedemnaście", "osiemnaście",
                  "dziewiętnaście"]
  
    dziesiat = ["","","dwadzieśćia", "trzydzieści", "czterdzieści",
                     "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt",
                     "dziewięćdziesiąt"]
  
    set = ["","sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset","siedemset", "osiemset", "dziewięćset"]
  
  
    if (l == 1):
        return cyfra[int(liczba)]

    if int(liczba) in range(10,20):
        return nascie[int(liczba)-10]

    if (l == 2):
        #list dzieli na char array
        liczbaIndex = list(liczba)
        return dziesiat[int(liczbaIndex[0])] + " " + cyfra[int(liczbaIndex[1])]
        
    if(l == 3):
     	liczbaIndex = list(liczba)
     	if(int(liczbaIndex[1]) == 1):
     		return set[int(liczbaIndex[0])] + " " + nascie[int(liczba[1]) + int(liczba[2]) - 11]
     	return set[int(liczbaIndex[0])] + " " + dziesiat[int(liczbaIndex[1])] + " " + cyfra[int(liczbaIndex[2])]
     
    if(l == 4):
     	liczbaIndex = list(liczba)
     	if(int(liczbaIndex[2]) == 1):
     		return "tysiąc " + set[int(liczbaIndex[1])] + " " + nascie[int(liczba[2]) + int(liczba[3]) - 11]
     	return "tysiąc " + set[int(liczbaIndex[1])] + " " + dziesiat[int(liczbaIndex[2])] + " " + cyfra[int(liczbaIndex[3])]
     	
     

print(zmienLiczbeNaStr("1811"))
