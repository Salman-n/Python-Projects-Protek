print("Pak Amir Menempuh Waktu kota A ke c adalah ?")

waktuAwal = float(06.00)
waktuJeda = float(0.45)

jarakAB = int(125)
jarakBC = int(256)

Kecepatan1  = int(62)
Kecepatan2  = int(70)

waktuAB    = round(jarakAB / Kecepatan1)
waktuBC    = round(jarakBC / Kecepatan2)

Waktusampai = waktuAwal + waktuAB + waktuBC + waktuJeda 
print("Waktu sampai di Kota C => ", Waktusampai)
