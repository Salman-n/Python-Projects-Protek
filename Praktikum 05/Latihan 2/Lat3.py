# program bil ganjil
z = 0
banyak = 0
jumlah = 0
while (z < 100) :
    for z in range(0,100):
      if(z % 2 == 1):
        print(z)
        z = z + 1
        jumlah = jumlah + z - 1
        banyak = z // 2
        
print("Banyak Bil Ganjil :", banyak)
print("Jumlah Bil Ganjil :", jumlah)
       
           
    
       
