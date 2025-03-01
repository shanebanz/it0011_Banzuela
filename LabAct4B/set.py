# Our Sets
A = {'a', 'b' , 'c', 'd' , 'f' , 'g'}
B = {'c', 'b', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. How many elements are there in set A and B
elementsTotal = len(A) + len(B);
print("Total number of elements in set A and B: " + str(elementsTotal))
# b. How many elements are there in B that is not part of A and C
elementsB = B - (A | C)  
elementCntr = len(elementsB)
print("Total number of elements in set B that is not part of A and C is: " + str(elementCntr))  

# c. Show the following using set operations
# & FOR INTERSECTION, - TO MINUS OR REMOVE A CERTAIN SET, | IS THE UNION, sorted() to sort it from a - z
# i. [h, i, j, k]
print(sorted(C - A))
# ii. [c, d, f]
print(sorted(A & C))
# iii. [b, c, h]
print(sorted((A & B) | (B & C)))
# iv. [d, f]
print(sorted(A & C - B))
# v. [c]
print(sorted(A & B & C))
# vi. [l, m, o]
print(sorted(B - (A | C)))