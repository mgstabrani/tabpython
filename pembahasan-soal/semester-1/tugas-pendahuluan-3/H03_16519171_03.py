# NIM/Nama  : 16519171/Mgs. Tabrani
# Tanggal   : 22 Oktober 2019
# Deskripsi : Tugas Pendahuluan 3 Nomor 3

#ProgramStringPalindrom
#Menerima masukan sebuah string dan menetukan apakah string tersebut palindrom

#KAMUS
#string : str
#string_reverse : [array of reverse of variabel string] 

#ALGORITMA

#Menerima masukan string
string = str(input("Masukkan string: "))

#Membalik/reverse masukan string
string_reverse = string[::-1]

#Menampilkan apakah string palindrom atau bukan
#Jika string palindrom
if (string == string_reverse):
    print(str(string) + " adalah palindrom")
#Jika string tidak palindrom
else:
    print(str(string) + " bukan palindrom")
