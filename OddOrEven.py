#Odd Or Even
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Enter a number: \n"))

mod = num % 2
mod4 = num % 4

if mod == 0:
    print("The number", num, "is even")
else:
    print("The number", num, "is odd")
if mod4 == 0:
    print("The number", num, "is multiple of 4")
else:
    print("The number", num, "is not multiple of 4")

check = int(input("Enter a check number: \n"))
result = check % num

if result == 0:
    print("The number", check, "is divided by ", num)
else:
    print("The number", check, "is not divided by ", num)