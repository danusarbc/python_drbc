#Entrar com o número e a base em que se deseja calcular o logaritmo.
import math
num = int(input("Entre com um número: "))
base = int(input("Entre com uma base logarítma: "))
log = math.log(num, base)
print("Logaritmo no número", num, "na base",base, "é: ", log)