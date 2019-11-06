#100quilowats custa 1/7 do salario minimo
#receba o valor do salario minimo e a quantidade de quilowats gasta em uma residencia
#calcule valor em reais de cada quilowatt, o valor em reais a ser pago, o novo valor a ser pago com um
#desconto de 10%

salary = float(input("Enter the minimum salary: "))
qtdQuilowatts = float(input("Enter the amount of quilowatts: "))

priceReal = (salary/7) / 100

totalValue = priceReal * qtdQuilowatts

discount = totalValue - (totalValue * 10)/100

print(round(priceReal,2))
print(round(totalValue,2))
print(round(discount,2))