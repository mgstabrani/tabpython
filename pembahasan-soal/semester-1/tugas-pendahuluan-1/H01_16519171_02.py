'''This program is a simple calcultaor which can do addition, subtraction,
multiplication, division, and modulo'''

A = float(input("Please, input the first number : ")) #a float 
B = float(input("Please, input the second number : ")) #a float
C = str(input("Please, input the operator : ")) #operator

if (C == "+"): 
	print("Result = " + str(A + B)) 
elif (C == "-"):
	print("Result = " + str(A - B)) 
elif (C == "x"):
	print("Result = " + str(A * B)) 
elif (C == ":"):
	print("Result = " + str(A / B))
elif (C == "%"):
	print("Result = " + str(A%B)) 
else:
	print("ERROR") #an error input of operator