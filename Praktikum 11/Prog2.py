from datetime import date 
import datetime
from dateutil.relativedelta import relativedelta

print("Selamat datang di Program Input KodeMember, NamaMember, JudulBuku")
print("-"*80)

def tglBukuPinjaman(set7hari):
     set7hari = date.today()
     return set7hari+relativedelta(days = 7) 

out = "";


while True:
        Member   = str(input("Masukan Kode Member  : "))
        NamaMember  = input("Masukan Nama Member  : ")
        JudBuku     = input("Masukan Judul Buku   : ")
        print("")
        set7hari = date.today()
        tambahlagi = str(input("Ulangi input lagi (y/n) : "))
        out = out + "|{}|{}|{}|{}|{}".format(Member, NamaMember ,JudBuku, set7hari, tglBukuPinjaman(set7hari)) + "\n"

        if (tambahlagi == 'y'):
             continue
        elif (tambahlagi == 'n'):
             break
print(out)

teks = out
file = open("DaftarPeminjam.txt","a")
file.write(teks)
file.close()
