#Menentukan apakah sebuah string adalah palindrom

string = input("Masukkan string:")
panjangString = 0

#Panjang string
for karakter in string:
    panjangString += 1

#Menentukan string palindrom
palindrom = True
for i in range(panjangString):
    palindrom = palindrom and (string[i] == string[panjangString-(i+1)])

#Menampilkan hasil
if(palindrom):
    print(string + " adalah palindrom")
else:
    print(string + " bukan palindrom")