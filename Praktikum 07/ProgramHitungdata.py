n = 0
sum = 0
def ProgramHitungdata():
    print("|===================================|")
    print("| Program Hitung Rata-Rata Bro Bro  |")
    print("|===================================|")
    
while True:
    angka = int(input("Silahkan Masukan bil Bulat : "))
    try:
        n = n + 1
        sum = sum + angka
        ulang = input("Ulangi kembali (y/n) ? : ")
        if (ulang == 'n'):
            rataRata = sum/n
            print("Rata-Ratanya Adalah : ", rataRata)
            break
        if (ulang != 'y'):
            break
    except ValueError:
        print("Bukan termasuk dari bil Bulat")
print("|            Selesai, Skuy           |")
            
