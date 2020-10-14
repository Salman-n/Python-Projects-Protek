import math
print ("Liter Bensin yang diperlukan ?")
print ("=================================")
jarakTempuh = int(input("Masukan Jarak tempuh =>"))
literBensin = int(12)
Liter  = jarakTempuh / literBensin
#karena bawaan 50 L maka
banyakIsi = (Liter-50) / 50 
print ("Maka Banyak Isi Bensin => ",math.ceil(banyakIsi), "liter")
print ("=================================")

   
