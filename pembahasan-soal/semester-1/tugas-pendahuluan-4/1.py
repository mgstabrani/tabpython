#Buat fungsi x^2 - 2x + 5
def f(x):
    return x**2 - 2*x + 5

#Variabel batas bawah dan batas atas
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

#Menampilkan f(A) sampai f(B)
for i in range(A,B+1):
    print("f(" + str(i) + ") = " + str(f(i)))