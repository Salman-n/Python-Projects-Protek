print("Selamat datang di Program Input NIM, Nama, Alamat Mhs")
print("-"*30)

teks = "";


while True:
        NIM        = str(input("Masukan NIM             : "))
        Nama       = str(input("Masukan Nama Mhs        : "))
        Alamat     = str(input("Masukan Alamat          : "))
        print("")
        tambahlagi = str(input("Ulangi input lagi (y/n) : "))

        teks = teks + "|{}|{}|{}".format(NIM, Nama ,Alamat) + "\n"

        if (tambahlagi == 'y'):
             continue
        if (tambahlagi == 'n'):
             break


# buka file untuk ditulis
Bukafile = open('2.txt', 'a')

# tulis teks ke file
Bukafile.write(teks)
Bukafile.seek(0, 0)
# tutup file
Bukafile.close()
