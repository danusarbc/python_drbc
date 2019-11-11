#Entrar com os numeros x1,x2 e x3
#Encontre x tal que
# x = x1 + (x2/x3+x1) + 2(x1-x2) + log de 64 na base 2
import math as m

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
x3 = float(input("Enter x3: "))

x = x1 + (x2/(x3+x1)) + 2*(x1-x2) + m.log(64,2)

print("X: ", x)

