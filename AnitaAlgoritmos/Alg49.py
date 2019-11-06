#Entrar com um nome e imprimir
#todo o nome
#primeiro caractere
#ultimo caractere
#do primeiro até o terceiro
#quarto caractere
#todos menos o primeiro
#os dois ultimos

character = input("Enter a character: ")

print("The character: ", character)
print("First: ", character[0])
print("Last: ", character[-1])
print("First to Third: ", character[:3])
print("Fourth: ", character[3])
print("Least the last: ", character[0:-1])