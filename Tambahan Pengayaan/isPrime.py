def ifopPrime(x):
    angka = 0
    pilih = "ya" or "tidak"
while True:
    x = int(input("masukan angka : "))
    print("------------")
    """Dibatasi sampai angka 200 aja bro, biar tidak banyak """
    if(x >= 200 ):
        print("batas input sudah maks, bro")
        continue
    elif(x > 1):
        print("apakah",x,"Bil prima ?")
        for perhitungan in range(1,x):
             angka = x - perhitungan
             if(x % angka != 0):
                print(angka,"membagi habis",x,'?', False) 
                continue
                print("Kesimpulan :",x, "Bukan Bil Prima")
             elif(x % angka == 0):
                print(angka,"membagi habis",x,'?', True)
                break
        if(angka == 1):
             print("kesimpualnnya adalah",x,"bil Prima bro")
        else:
             print("kesimpulannya adalah",x,"bukan Prima bro")
    else:
        print(x,"bukan bil Prima, karena bil prima harus >= dari", x)
        
         
