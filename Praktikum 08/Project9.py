print("*"*5,"Menu Harga Buah-Buahan","*"*5)
DaftarBuahBuahan = {
    "apel" : 5000,
    "jeruk" : 8500,
    "mangga" : 7800,
    "duku" :6500
}

print(DaftarBuahBuahan)
print("-"*50)
def BeliBuah():
    memilih = input("Nama buah yang dibeli  = ")
    while True :
        try:
            if  memilih in DaftarBuahBuahan :
                masukanBerat = float(input("Silahkan Masukan Total Buah yang akan anda beli :"))
                print("Total buah yang akan di beli (Kg) :", masukanBerat,"Kg")
                print("="*50)
                print("Total Harga bayar : Rp.", DaftarBuahBuahan[memilih] * masukanBerat)
                break
            else :
                print("Nama Buah tidak terdaftar")
                break        
        except:
            print("Inputan berat bukan menggunakan koma")
            break

BeliBuah()
        
        
        
