print("A). \n")

for i in range(1,6):
    
    for j in range(1,6-i):
        print(" ", end="")
        
    for x in range(1, i+1):
        print(x, end="")
    
    print()

print("\nB). ")

#change from for loop to while loop
i = 0
while i < 7:
    j = 0
    while j <= i:
        if i == 1:
            break
        elif i == 5:
            break
        else:
            print(end="")
        print(i + 1, end=" ")
        j += 1
    print()
    i += 1

# for i in range(0,5):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print() 
# basic number loop
# 1
# 12
# 123
# 1234
# 12345

#a).
#     1
#    12
#   123
#  1234
# 12345

# print((i+1-x), end="") (I used this for experimental purposes)