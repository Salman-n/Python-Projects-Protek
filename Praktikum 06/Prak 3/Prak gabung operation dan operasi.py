#Menghitung Operasi + / X -
from operation import*
a,b = 2,4
c,d = 6,4
print("A =>",kurang(jumlah(kali(b,c),a),d))

a,b = 4,7
c,d = 6,9
print("B =>",kali(jumlah(a,b),kurang(c,d)))

a,b = 10,2
c,d = 7,5
e,f = 12,34
print("C =>",bagi(bagi(jumlah(a,b),jumlah(c,d)),kurang(e,f)))
