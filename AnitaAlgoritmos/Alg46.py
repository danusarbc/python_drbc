#Entrar com um saldo de uma aplicação e imprimir o novo saldo, considerando o reajuste de 1%

saldo = float(input("Qual seu saldo em conta? "))
rendimento = saldo + (saldo * 1)/100

print("Seu novo saldo após o rendimento de 1% é: ", rendimento)
