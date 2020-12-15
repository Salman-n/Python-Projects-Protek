from math import floor
import math
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50 , 'uas' : 80}, 
         {'nim' : 'A02', 'nama' : 'Budi'    , 'mid' : 40 , 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha'  , 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna'   , 'mid' : 20 , 'uas' : 100}, 
         {'nim' : 'A05', 'nama' : 'Fatimah' , 'mid' : 70 , 'uas' : 100}]


bar1 = "NIM"
bar2 = "Nama"
bar3 = "N.MID"
bar4 = "N.UTS"
bar5 = "N.AKHIR"
bar6 = "STATUS"

nil= floor((nilai[0]['mid'] + 2 * nilai[0]['uas'])/3)
nil1= floor((nilai[1]['mid'] + 2 * nilai[1]['uas'])/3)
nil2= math.ceil((nilai[2]['mid'] + 2 * nilai[2]['uas'])/3)
nil3= floor((nilai[3]['mid'] + 2 * nilai[3]['uas'])/3)
if (nil < 60 and nil1 < 60 and nil2 < 60 and nil3 < 60) :
     status = "TIDAK LULUS"
else :
     status = "LULUS"

print("="* 70)
print(bar1.rjust(0), bar2.rjust(9), bar3.rjust(13), bar4.rjust(9), bar5.rjust(13), bar6.rjust(9))
print("-"* 70)


print(nilai[0]['nim'],'\t',nilai[0]['nama'],'\t',nilai[0]['mid'],'\t  ',nilai[0]['uas'],'\t        ',     nil,'   ', status)
print(nilai[1]['nim'],'\t',nilai[1]['nama'],'\t\t',nilai[1]['mid'],'\t  ',nilai[1]['uas'],'\t        ',   nil1,'   ',status)
print(nilai[2]['nim'],'\t',nilai[2]['nama'],'       ',nilai[2]['mid'],'\t  ',nilai[2]['uas'],'\t        ',nil2,'   ',status)
print(nilai[3]['nim'],'\t',nilai[3]['nama'],'\t\t',nilai[3]['mid'],'     ',nilai[3]['uas'],'\t        ',  nil3,'   ',status)

print("-"* 70)
