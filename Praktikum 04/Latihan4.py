import math
print("Pak Amir Menempuh Waktu kota A ke C adalah ?")
print("=======================================")
waktuAwal = int(6)
waktuJeda = int(45)

jarakAB = int(125)
jarakBC = int(256)

Kecepatan1  = int(62)
Kecepatan2  = int(70)

waktuAB    = (jarakAB / Kecepatan1)
waktuBC    = (jarakBC / Kecepatan2)

Waktutempuh = math.ceil((waktuAB + waktuBC) * 60) + waktuJeda
totalWaktu  = math.ceil(Waktutempuh // 60) + (Waktutempuh % 60) / 100 + waktuAwal
print("=======================================")
print("Waktu sampai di Kota C => ", totalWaktu)

