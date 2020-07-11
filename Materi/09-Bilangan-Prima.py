#Bilangan Prima
#Bilangan bulat positif yang tidak habis dibagi oleh bilangan lain, selain 1 dan bilangan itu sendiri
#Menentukan apakah suatu bilangan itu prima, 2,3,5,7,11,....

n = int(input())    #asumsi n lebih dari 1
prima = True
for i in range(2,n):
    if (n % i  == 0):
        prima = False
print(prima)       
        
