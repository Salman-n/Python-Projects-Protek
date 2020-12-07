# Meminta input angka batas bawah dan batas atas

angka1 = int(input("Masukkan batas bawah: "))
angka2 = int(input("Masukkan batas atas: "))
def sqNumbers (angka1, angka2):
        bilangan = 0
# membangkitkan bilangan prima

        for bilrange in range(angka1,angka2):
                    for bilangan in range (angka2):
                            if (bilrange == bilangan ** 2):
                                   print (bilrange)

sqNumbers(angka1,angka2)
