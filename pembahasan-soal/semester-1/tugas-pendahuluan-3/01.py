#Menerima input N bilangan bulat, kemudian menampilkan bilangan tersebut secara terbalik dari urutan input

N = int(input())    #Jumlah bilangan
bilangan = [int for i in range(N)]  #array bilangan

#Input N bilangan
for i in range(N):
    bilangan[i] = int(input())

#Menampilkan bilangan secara urutan terbalik dari input
for i in range(N-1,-1,-1):
    print(bilangan[i])