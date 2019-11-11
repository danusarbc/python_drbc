#Encontrar a razao de uma PA e o valor do 1 termo
#encontre o decimo termo
#encontr o quinto termo da PG

import math as m

first_term = float(input("Enter a first term: "))
common_difference = float(input("Enter a common difference: "))

dec_term = first_term + 9*common_difference
fifth_term = first_term + m.pow(common_difference,4)

print("Tenth term -  PA: ", dec_term)
print("Fifth_term -  PG: ", first_term)

