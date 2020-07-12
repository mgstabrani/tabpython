'''This program requires an input of N (N is an integer).
Then it will display the smallest of 10^x and more than N.'''

N = int(input("Please, input N: "))
stop = False
i = 0

while (stop == False):
    if (N<10**i):
        stop = True
    else :
        i = i + 1
        
print(10**i)
