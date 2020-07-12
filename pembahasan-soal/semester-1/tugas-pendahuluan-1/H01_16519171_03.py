'''
This program is to determine weather the number is positive, negative, odd, or even
'''

X = int(input("Input X : ")) 

if (X > 0): 
	if (X%2 == 0):
		print("X is a positive and even number") 
	else:
		print("X is a positive and odd number") 
elif (X < 0): 
	if (X%2 == 0):
		print("X is a negative and even number") 
	else:
		print("X is a negative and odd number") 
else: 
	print("X is zero")

