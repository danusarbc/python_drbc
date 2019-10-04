#Character Input
#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

name = input("Enter your name: \n")
age = int(input ("Enter your age: \n"))
yearNow = datetime.datetime.now()
year = yearNow.year + (100-age)
print(name, "you will complete 100 years old in: ", year)

number = int(input("Enter a number \n"))
for i in range(0,number):
    print(i, "-", name, "you will complete 100 years old in: ", year)

