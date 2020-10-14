print("Tarif Sewa")
print("==========================================")
print ("Sewa mobil /12 jam          => Rp 200000")
print ("Sewa mobil /jam             => Rp 10000" )
print("==========================================")
sewaPertama = 200000
sewaTambah = 10000

jamPertama = float(06.00)
jamKedua   = int(23.50)
hasilJam = round(jamKedua - jamPertama)

waktuSewa = int(12)
waktuTambahan = hasilJam - waktuSewa

biayaTambah = waktuTambahan * 10000
total = sewaPertama + biayaTambah
print("==========================================")
print("biaya sewa pertama          => Rp",sewaPertama)
print("biaya sewa tambahan         => Rp",biayaTambah)
print("Total biaya sewa            => Rp",total)
print("==========================================")
