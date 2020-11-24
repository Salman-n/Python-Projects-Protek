def DaftarNama():   
    DaftarNamaMhs = []
    nomor = 0
    while True:
        inpNama = (input("Silahkan Input nama : "))
        nomor += 1
        tambahNama = input("Menambah input nama kembali (y/n) ? ")
        DaftarNamaMhs.append(inpNama)
        if (tambahNama == 'y'):
            continue
        else:
            break
    print("")
    print("|--------||---------||--------|")
    print("|        Tampilan Nama        |")
    print("|--------||---------||--------|")

    DaftarNamaMhs.sort()
    A = 0
    while True:
        for Jn in DaftarNamaMhs:
            A += 1
            print(str(A) + ". " + Jn.capitalize() + " (" + str(len(Jn)) + " karakter)")
            
        break        
DaftarNama()

