#Check Primality Functions

#Ask the user for a number and determine whether the number is prime or not. 
#(For those who have forgotten, a prime number is a number that has no divisors.).

def primeNumber(num):
    if num == 1:
        prime = False
    elif number == 2:
        prime = True
    else:
        prime = True
        for x in range(2,num):
            if num % x == 0:
                prime = False
                break
    return prime

number = int(input("Enter a number \n"))

result = primeNumber(number)

if result:
    print(number, "is prime")
else:
    print(number, "is not prime")