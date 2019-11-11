#Entrar com os valores do catetos e encontrar a hipotenusa

import math as m

leg_1 = float(input("Enter a first leg: "))
leg_2 = float(input("Enter a second leg: "))

hypotenuse = m.sqrt(leg_1**2 + leg_2**2)

print("Hypotenuse: ", round(hypotenuse,2))

