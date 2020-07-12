# NIM/Nama  : 16519171/Mgs. Tabrani
# Tanggal   : 22 Oktober 2019
# Deskripsi : Tugas Pendahuluan Praktikum 3 Nomor 1

#ProgramBilanganTerbalik
#Menerima N buah bilangan dan menampilkannya serta menampilkannya kembali dengan urutan yang terbalik

#KAMUS
#Banyak_Bilangan, i : int
#Elemen_Bilangan : [array of int]

#ALGORITMA

#Inisiasi banyak bilangan dan membuat array
Banyak_Bilangan = int(input("Masukkan N: "))
Elemen_Bilangan = [int for i in range(Banyak_Bilangan)]

#Mengisi array
for i in range(Banyak_Bilangan):
    Elemen_Bilangan[i] = int(input())

#Menampilkan array yang terbalik
print("Hasil dibalik: ")
for i in range(Banyak_Bilangan-1,-1,-1):
    print(Elemen_Bilangan[i])
    
    
