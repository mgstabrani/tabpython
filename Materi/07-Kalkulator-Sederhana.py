#Kalkulator Sederhana
# Constraint = operator(+,-,*,/), hanya dua bilangan

a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
operator = input("Masukkan operator")
if (operator == "+"):
    print(a+b)
elif (operator == "-"):
    print(a-b)
elif (operator == "/"):
    print(a/b)
elif (operator == "*"):
    print(a*b)
else:
    print("Syntax error")
