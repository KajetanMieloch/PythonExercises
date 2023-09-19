#Lista 9 grupa 3 zadanie 3
import numpy as np
print("Prosze podać następujące dane: ")
v0 = float(input("Prędkość początkowa: "))
katStop = float(input("Kąt rzutu (stopnie): "))

katRad = np.pi/2
g = 9.81

hMax = (v0**2.0/2.0*g)*(np.sin(katRad)**2.0)
zasieg = (v0**2.0/2.0*g)*(np.sin(2.0*katRad))
czas = (2.0*v0/g)*(np.sin(katRad))

print("Maksymalna wysokość:", hMax,"Maksymalny zasięg:", zasieg, "Czas lotu:", czas)
