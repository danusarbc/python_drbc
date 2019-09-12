#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

word = input("Enter a string: \n")

if word == word[::-1]:
    print("The word", word, "is palindrome")
else:
    print("The word", word, "is not palindrome")
