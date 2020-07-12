# NIM/Nama : 16519171/Mgs. Tabrani
# Tanggal : 8 Oktober 2019
# Deskripsi : Program_Bilangan_Prima
#Menentukan_bahwa_Masukan_Bilangan_Prima_atau_Bukan

#Kamus
#X, i : int
#stop : boolean

#Algoritma
X = int(input("Masukkan X: "))
i = 2
stop = False

if (X < 2):
    print(str(X) + " bukan bilangan prima") #Jika X kurang dari 2 bukan bilangan prima

else:
    for i in range(2,X):
        if (X%i == 0):
            stop = x
        else :
            i = i+1
    if (stop == True) :
        print(str(X) + " bukan bilangan prima")
    else:
        print(str(X) + " adalah bilangan prima")

    
