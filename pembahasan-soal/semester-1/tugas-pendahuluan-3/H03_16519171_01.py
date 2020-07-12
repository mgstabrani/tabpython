'''This program requires an array of integer, which firstly the length
of array is required. The program will display the reversed of array'''


#Input the length of array and inisialize array
N = int(input("Input N: "))
elemenArray = [int for i in range(N)]

#Fill the array
for i in range(N):
    elemenArray[i] = int(input())

#Display the reversed array
print("Reversed array: ")
for i in range(N-1,-1,-1):
    print(elemenArray[i])
    
    
