#Menerima dua array, A dan B, kemudian menentukan apakah A dan B anagram, menggunakan tabel frekuensi, elemen A dan B hanya 1-10

#Membuat tabel frekuensi
tabelFrekA = [0 for i in range(10)]
tabelFrekB = [0 for i in range(10)]

#Input nilai
banyakA = int(input("Masukkan banyaknya elemen A: "))
for i in range(banyakA):
    elemenA = int(input("Masukkan elemen A ke-" + str(i+1) + ": "))
    tabelFrekA[elemenA-1] += 1
banyakB = int(input("Masukkan banyaknya elemen B: "))
for i in range(banyakB):
    elemenB = int(input("Masukkan elemen B ke-" + str(i+1) + ": "))
    tabelFrekB[elemenB-1] += 1

#Penentuan anagram
anagram = True
if(banyakA == banyakB):
    for i in range(10):
        anagram = anagram and (tabelFrekA[i] == tabelFrekB[i])
else:
    anagram = False

#Menampilkan hasil
if(anagram):
    print("A adalah anagram dari B")
else:
    print("A bukan anagram dari B")