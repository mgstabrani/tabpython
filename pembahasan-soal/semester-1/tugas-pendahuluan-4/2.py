#Variabel N(baris) dan M(kolom)
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))

#Inisiasi matriks NxM
matriks = [[0 for j in range(M)] for i in range(N)]

#Inisiasi jumlah elemen positif di matriks
countPositif = 0

#Mengisi matriks sambil menghitung jumlah elemen positif
for i in range(N):
    for j in range(M):
        matriks[i][j] = int(input("Masukkan nilai A[" + str(i+1) + "][" + str(j+1) + "]: "))
        if(matriks[i][j] > 0):
            countPositif += 1

#Menampilkan jumlah elemen positif matriks dan isi matriks keseluruhan
print("Ada " + str(countPositif) + " bilangan positif di matriks.")
for i in range(N):
    for j in range(M):
        print(matriks[i][j], end=" ")
    print()