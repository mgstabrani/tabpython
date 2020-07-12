'''This program requires a string then the program will display
weather the string is palindrom or not'''

string = str(input("Please, input string: "))

#Reverse the string
stringReverse = string[::-1]

#Display weather the string is palindrom or not
if (string == stringReverse):
    print(str(string) + " is palindrom")
else:
    print(str(string) + " is not palindrom")
