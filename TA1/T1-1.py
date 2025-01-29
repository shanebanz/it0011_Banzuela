# 1. A program that will display the number of vowels, consonants, spaces, and other characters 
# given an input string. (use for loop and some operators under module 1 and 2)

userInput = input("Enter a string: ")

vowCount = 0
consCount = 0
spcCount = 0
othersCount = 0


# they can be typed UPPERCASE or LOWERCASE
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" 


# for every character, check if it belongs to one of the options and add it to their counter var
for char in userInput:
    if char in vowels:
        vowCount += 1
    elif char in consonants:
        consCount += 1
    elif char == ' ':
        spcCount += 1
    else:
        othersCount += 1
        
print("Number of vowels in user input: ", vowCount)
print("Number of consonants in user input: ", consCount)
print("Number of spaces in user input: ", spcCount)
print("Number of others in user input: ", othersCount)
        