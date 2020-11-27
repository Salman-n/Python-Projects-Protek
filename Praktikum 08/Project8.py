daftarharga = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
 
def rataharga():
    jumlahBuah = 0
    jumlahHarga = 0
    Rata = 0
    for key,value in daftarharga.items():
          jumlahHarga += value
          jumlahBuah += 1

    Rata = jumlahHarga / jumlahBuah
    print("Rata-Rata Harga buah adalah", Rata)

rataharga()
