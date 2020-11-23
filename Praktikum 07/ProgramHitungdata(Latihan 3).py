sum = 0
bil = 0
def ProgramHitungdata():
    print("|===================================|")
    print("| Program Hitung Rata-Rata Bro Bro  |")
    print("|===================================|")
    
while True:
    angka = int(input("Silahkan Masukan bil Bulat : "))
    try:
        bil = bil + 1
        sum = sum + angka
        ulang = input("Ulangi kembali (y/n) ? : ")
        if (ulang == 'n'):
            rataRata = sum/bil
            print("Rata-Ratanya Adalah : ", rataRata)
            break
        if (ulang != 'y'):
            break
    except ValueError:
        print("Bukan termasuk dari bil Bulat")
print("|            Selesai, :D       |")
            
