"""Keterangan"""
# inpBil (Input Bilangan)
daftarAngka = []
print("=========================================================")
AngkaInput = int(input("Silahkan Masukan jumlah bilangan bulat :  "))
print("=========================================================")
def decentAngka():
    bil = 0
while True :
    for bil in range (0,AngkaInput):
           bil = bil + 1
           try:
               inpBil = int(input("Silakan Masukan Angka k-" + str(bil) + '   =>'))
               daftarAngka.append(inpBil)
           except:
               print("Bukan termasuk dari bil bulat")
    daftarAngka.sort(reverse=True)
    print(daftarAngka)
    break
                   
