print("Cara Pertama :")
def UbahHurufdariKata(str1, a, b):
    print("Hasil Ubah huruf dalam kata", str1)
    Strng = str1 
    for katadalamstr1 in range(len(a)):
          ubah = Strng.replace(a[katadalamstr1],b[katadalamstr1])
          print("-"*25)
          print(ubah)
          print("-"*25)
          
UbahHurufdariKata("MATEMATIKA", "T", "S")
print("")
print("Cara Kedua :")
def UbahHurufdariKata(str1, a, b):
    print("Hasil Ubah huruf dalam kata", str1)
    stringbaru = ""
    for ubah in str1:
        if ubah == a:
            stringbaru = stringbaru + b
        else:
            stringbaru = stringbaru + ubah
    print("-"*25)
    print(stringbaru)
    print("-"*25)
          
UbahHurufdariKata("MATEMATIKA", "T", "S")


