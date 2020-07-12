# NIM/Nama  : 16519171/Mgs. Tabrani
# Tanggal   : 22 Oktober 2019
# Deskripsi : Tugas Pendahuluan Praktikum 3 Nomor 2

#ProgramAnagramArray
#Membuat Array A dan B, memeriksa apakah A adalah anagram dari B

#KAMUS
#Banyak_A, Banyak_B, i, j : int
#A, B : [array of int]

#ALGORITMA

#Memasukkan banyak elemen array A dan membuat Array A
Banyak_A = int(input("Masukkan banyaknya elemen A: "))
A = [int for i in range(Banyak_A)]
#Mengisi Array A
for i in range(Banyak_A):
    A[i] = int(input("Masukkan elemen A ke-" +str(i+1) + ": "))

#Memasukkan banyak elemen array B dan membuat Array B
Banyak_B = int(input("Masukkan banyaknya elemen B: "))
B = [int for j in range(Banyak_B)]
#Mengisi Array B
for j in range(Banyak_B):
    B[j] = int(input("Masukkan elemen A ke-" +str(j+1) + ": "))

#Menampilkan apakah A anagram dari B
#Jika A anagram dari B
if (sorted(A)== sorted(B)):
    print("A adalah anagram dari B")
#Jika A bukan anagram dari B
else:
    print("A bukan anagram dari B")
