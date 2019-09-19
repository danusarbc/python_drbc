#Fibonacci
def Fibonacci(num):
    if num <=1:
        return num
    else:
        return Fibonacci(num -1) + Fibonacci(num - 2)

fib = int(input("Enter a number: "))

result = Fibonacci(fib)

print ("Fibonacci number:", result)