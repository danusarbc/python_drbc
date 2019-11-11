#Entrar com o valor hora aula, numero de aulas dadas no mes e percentual de desconto do INSS


#tabela INSS
#até 1.751,81 - 8%
#de 1.751,82 até 2.919,72 - 9%
#de 2.919,73 até 5.839,45 - 11%
import math as m

hour_value = float(input("Enter a value of an hour: "))
class_days = int(input("Enter a quantity of classes in a month: "))

gross_salary = hour_value * class_days
print("Gross salary: ", gross_salary)

if gross_salary <= 1751.81:
    net_salary = gross_salary - gross_salary*0.08
    print("Net salary: ", net_salary)
elif gross_salary >= 1751.82 and gross_salary <=2919.72 :
    net_salary = gross_salary - gross_salary*0.09
    print("Net salary: ", net_salary)
elif gross_salary >= 2919.73 or gross_salary>= 5839.45 :
    net_salary = gross_salary - gross_salary*0.11
    print("Net salary: ", net_salary)


