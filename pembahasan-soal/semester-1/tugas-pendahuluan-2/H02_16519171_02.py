# NIM/Nama : 16519171/Mgs. Tabrani
# Tanggal : 8 Oktober 2019
# Deskripsi : Program_Bilangan_Basis_10
#Menampilkan_Bilangan_Basis_10_terkecil_yang_Lebih_Besar_dari_Masukan

#Kamus
#N, i : int
#stop : boolean

#Algoritma
N = int(input("Masukkan N: "))
stop = False
i = 0

while (stop == False):
    if (N<10**i):
        stop = True
    else :
        i = i + 1
        
print(10**i)
