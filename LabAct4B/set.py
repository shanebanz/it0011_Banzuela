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