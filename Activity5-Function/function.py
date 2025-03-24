def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return None
    return num1 / num2

def exponentiation(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    if num2 == 0:
        print("Cannot find remainder with zero")
        return None
    return num1 % num2

def summation(num1, num2):
    if num2 < num1:
        print("Second number must be greater than first number")
        return None
    
    total = 0
    for i in range(num1, num2 + 1):
        total += i
    return total

print("Mathematical Operations")
print("[D] - Divide")
print("[E] - Exponentiation")
print("[R] - Remainder")
print("[F] - Summation")
print("[Q] - Quit")

while True:
    choice = input("Enter your choice: ").upper()
    
    if choice == 'Q':
        print("Program ended")
        break
    
    if choice not in ['D', 'E', 'R', 'F']:
        print("Invalid choice")
        continue
    
    if choice in ['D', 'E', 'R']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 'D':
            result = divide(num1, num2)
        elif choice == 'E':
            result = exponentiation(num1, num2)
        else:
            result = remainder(num1, num2)
    
    else: 
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = summation(num1, num2)
    
    if result is not None:
        print("Result:", result)