file = open("TechnicalME/numbers.txt", 'r')
lines = file.readlines()
file.close()

line_number = 1
for line in lines:
    numbers = line.strip().split(',')
    total_sum = 0
    
    for num in numbers:
        if not num.isdigit():
            break
        total_sum += int(num)
    else:
        print("Line", line_number, ":", line.strip(), "(sum", total_sum, ") -", "Palindrome" if str(total_sum) == str(total_sum)[::-1] else "Not a palindrome")
    
    line_number += 1