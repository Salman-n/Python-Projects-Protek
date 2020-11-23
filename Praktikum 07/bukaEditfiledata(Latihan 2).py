namaDariFile = str(input("Silahkan anda masukan nama file : "))
def bukaTambahFileData():
        namaDariFile = str(input("Silahkan anda masukan nama file : "))
try :
        while True :
            filenya = open(namaDariFile, "a")
            datanya = input("Data yang ingin ditambahkan kembali (y/n) ? :")
            filenya.write(datanya +"\n")
            filenya.close()
            ulangi = input("Mau Lagi (y/n) ? : ")
            if ulangi == "n":
               break
            if ulangi != "y":
               print("Data tidak valid broo")
               break
except FileNotFoundError:
    print("Terjadi kesalahan, File data tidak ditemukan Broo")
    
