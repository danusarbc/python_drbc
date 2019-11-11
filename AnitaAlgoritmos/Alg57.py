#Entrar notas PR1 e PR2 e imprimir a media final
#truncada e arredondada
import math as m

pr1 = float(input("Enter a first grade: "))
pr2 = float(input("Enter a second grade: "))

AVG = (pr1 + pr2) /2

print("AVG: ", AVG)
print("AVG (truncate): ", m.trunc(AVG))
print("AVG (rounded): ", round(AVG))
