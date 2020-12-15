mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

bar1 = "NIM"
bar2 = "NAMA MAHASISWA"
bar3 = "TGL LAHIR"
bar4 = "TEMPAT LAHIR"

print("="* 90)
print(bar1.ljust(7), bar2.ljust(20), bar3.ljust(20), bar4.ljust(20))
print("-"* 90)

for pisahdata in mhs :
     pisah = pisahdata.split(":")
     tanggal = pisah[3].replace("-","/")
     print(pisah[0].ljust(7),pisah[1].ljust(20),pisah[2].ljust(20),pisah[3])
print("-"* 90)
