Namadarifile = str(input("Masukan nama file      : "))
print("|================================================|")
print("|        Program Pencarian File Anda             |")
print("|================================================|")
def pencarianFile():
    Namadarifile = str(input("Masukan nama file      : "))
try :
    print("Isi file", Namadarifile, " adalah : ")
    file = open(Namadarifile, "r")
    print(file.read())
except FileNotFoundError:
    print("terjadi kesalahan file tidak ditemukan")

print("<<===========================================>>")
