def UbahHurufdariKata(str1, a, b):
    Strng = str1 
    for katadalamstr1 in range(len(a)):
          ubah = Strng.replace(a[katadalamstr1],b[katadalamstr1])
          print("-"*25)
          print('Hasil Ubah Huruf dalam Kata', str1, 'adalah')
          print(ubah)
          print("-"*25)
          
UbahHurufdariKata("MATEMATIKA", "T", "S")
