print(""*5,"Menu Harga Buah-Buahan",""*5)
DaftarBuahBuahan = {
    "apel" : 5000,
    "jeruk" : 8500,
    "mangga" : 7800,
    "duku" :6500
}

print(DaftarBuahBuahan)
print("-"*50)
def BeliBuah():
    jmlTotal= 0
    while True :
        memilih = input("Nama buah yang dibeli  = ")
        if  memilih in DaftarBuahBuahan :
            masukanBerat = int(input("Silahkan Masukan Total Buah yang akan anda beli : "))
            print("Total buah yang akan di beli (Kg) :", masukanBerat,"Kg")
            print("="*50)
            print("_____")
            pil2 = str(input("Beli buah yang lain (y/n) ?  = "))
            jmlTotal += (DaftarBuahBuahan[memilih]*masukanBerat)
            if pil2 == "n":
                print("Total harga           : Rp.",jmlTotal)
                break
        else :
            print("Nama Buah tidak terdaftar")
            break
        
BeliBuah()
