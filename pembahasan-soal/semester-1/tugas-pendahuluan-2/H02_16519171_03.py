'''This program will determine weather a number is prime or not'''

X = int(input("Input X: "))
prime = True
if (X<2) :
    prime = False
else:
    for i in range(2,X):
        if (X % i == 0):
            prime = False

if (prime==True):
    print(X, "is prime number")
else:
    print(X, "is not prime number")




    
