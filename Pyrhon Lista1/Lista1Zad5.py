#Kajetan Mieloch

import math

def testowanieAiB(a,b):
    print("dla liczb: " + str(a) + " oraz " + str(b))
    print("wynik a/b: " + str(a/b))
    print("wynik a/b: " + str(a//b))
    print("Wynik round a/b: " + str(round(a/b)))
    print("Wynik floor a/b: " + str(math.floor(a/b)))
    print("")

testowanieAiB(5,2)
testowanieAiB(3,2)
testowanieAiB(3,5)

#a//b nie jest zaokrągleniem - usuwa wszystko po przecinku np: [1.2 => 1], [1.9 => 1]
#round jest zaokrągleniem w góre np: [1.5 => 2], [0.6 => 1]
#floor jest zaokrągleniem w dół np: [0.6 => 0], [1.5 => 1]
