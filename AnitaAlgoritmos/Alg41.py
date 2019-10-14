#Entrar com 4 numeros e imprimir a media ponderada. Pesos são: 1, 2, 3 e 4.

num1 = int(input("Entre com o primeiro número: "))
num2 = int(input("Entre com o segundo número: "))
num3 = int(input("Entre com o terceiro número: "))
num4 = int(input("Entre com o quarto número: "))

medPonderada = (num1*1 + num2*2 + num3*3 +num4*4)/10

print("A média ponderada entre", num1, ",", num2, ",", num3, "e", num4, "é:", medPonderada)