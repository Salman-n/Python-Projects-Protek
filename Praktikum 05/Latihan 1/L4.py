kode            = int(input("Masukan Kode Karyawan     => "))
Nama_Karyawan   = str(input("Masukan Nama Karyawan     => "))
golKar          = str(input("Masukan Golongan Karyawan => "))
if   (golKar == 'A'):
      Gajipokok = 10000000
      potonganGaji = 2.5
elif (golKar == 'B'):
      Gajipokok = 8500000
      potonganGaji = 2.0
elif (golKar == 'C'):
      Gajipokok = 7000000
      potonganGaji = 1.5
elif (golKar == 'D'):
      Gajipokok = 5500000
      potonganGaji = 1.0
else :
      print("Golongan Gaji tidak ditemukan")
      exit()
     
       
potongGaji = Gajipokok  * (potonganGaji / 100)
print("===================================================")
print("Masukkan Kode Karyawan     => ",kode)
print("Masukkan Nama Karyawan     => ",Nama_Karyawan)
print("Masukkan Golongan Karyawan => ",golKar)
print("===================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------------------")
print("Nama Karyawan              =>",Nama_Karyawan)
print("Golongan                   =>",golKar)
print("---------------------------------------------------")
print("Gaji Pokok                 => Rp.",Gajipokok)
print("Potongan   ({0}%)          => Rp.({1})".format(potonganGaji,potongGaji))
print("---------------------------------------------------")
print("Gaji Bersih                => Rp.",(Gajipokok - potongGaji))
print("----------------++++++====-----------------------")

    
