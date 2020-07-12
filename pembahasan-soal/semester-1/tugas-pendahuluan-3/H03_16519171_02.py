'''This program will detect weather the two arrays are panagram or 
not'''

#Inisialize an array named A
lengthOfA = int(input("Input the length of A: "))
A = [int for i in range(lengthOfA)]
#Fill the arrays
for i in range(lengthOf_A):
    A[i] = int(input("Input the-(" +str(i+1) + ") element of A: "))

#Inisializw an array named B
lengthOfB = int(input("Input the length of B: "))
B = [int for j in range(lengthOfB)]
#Fill the array
for j in range(lengthOfB):
    B[j] = int(input("Input the-(" +str(j+1) + ") element of B: "))

#Display weather the arrays are anagram or not
if (sorted(A) == sorted(B)):
    print("A is an anagram of B")
else:
    print("A is not an anagram of B")
