#Variabel N(baris dan kolom)
N = int(input("Masukkan N: "))

#Inisialisasi matriks dengan seluruh elemen bernilai 1
matriks = [[1 for j in range(N)] for i in range(N)]

#Mengisi matriks sesuai perintah soal 
'''
matriks[i-1][j] : elemen matriks sebelah kiri
matriks[i][j-1] : elemen matriks di atasnya
'''
for i in range(N):
    for j in range(N):
        if (i != 0 and j != 0):
            matriks[i][j] = matriks[i-1][j] + matriks[i][j-1]

#Menampilkan isi matriks
for i in range(N):
    for j in range(N):
        print(matriks[i][j], end=" ")
    print()