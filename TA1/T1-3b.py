i = 0
while i < 7:
    j = 0
    while j <= i:
        if i == 1 or i == 3:  
            break
        print(i + 1, end=" ")
        j += 1
    if i != 1 and i != 3:  
        print()  
    i += 1