#Modifikasi Kode prak 2.1
def luasSegitiga(alas,tinggi):
    luas = alas * tinggi // 2
    return luas

a = 10
t = 20
print ('Luas segitiga dg alas', a,
       'dan tinggi', t,
       'adalah ', luasSegitiga(a,t))

a2 = 15
t2 = 45
print ('Luas segitiga dg alas', a2,
       'dan tinggi', t2,
       'adalah ', luasSegitiga(a2,t2))
