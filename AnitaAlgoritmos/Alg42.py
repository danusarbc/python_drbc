#Entrar um angulo em graus e imprimir seno, co-seno, tangente, secante, co-secante e co-tangente
import math
angulo = int(input("Entre com um ângulo em graus: "))
rad = (angulo * math.pi) / 180
print("Seno: ", math.sin(rad))
print("Co-seno: ", math.cos(rad))
print("Tangente: ", math.tan(rad))
print("Secante: ", 1 / math.cos(rad))
print("Co-secante: ", 1 / math.sin(rad))
print("Co-tangente: ", 1 / math.tan(rad))