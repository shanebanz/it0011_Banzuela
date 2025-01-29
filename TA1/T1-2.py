#A program that will count the sum of the digits from a given input string digits. 
# (use for loop and some operators under module 1 and 2)

inputString = input("Enter input string digits: ")
digits = '0123456789'
digitSum = 0

for char in inputString:
    if char in digits:
        digitSum += int(char) # convert the currect character into a digit and start summing them up

print("Sum of the digits entered from a given string digits: ", digitSum)
