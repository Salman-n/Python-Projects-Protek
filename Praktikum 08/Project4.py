DaftSayur = ['bayam', 'kangkung', 'Wortel', 'selada']
def MenuSYR():
    
    print("--------- Menu ---------")
    print("A. Tambah data sayur")
    print("B. Hapus data sayur")
    print("C. Tampilkan data sayur")
    print("-------------------------")
    pilihMenu = input("Pilihan Anda   : ")

    while True :
        if pilihMenu == "A":
            inpSyrbaru = str(input("Tambahkan data sayur baru  : "))
            DaftSayur.append(inpSyrbaru)
            print(DaftSayur)
            break
        if pilihMenu == "B":
            try:
                DiHps = int(input("Pilih data sayur yang ingin dihapus (Pakai angka Ex: 1) : "))
                print(DaftSayur.pop(DiHps))
                break
            except ValueError:
                print("terjadi kesalahan data sayur tidak ditemukan")
                continue
        if pilihMenu == "C":
                print(DaftSayur)
                break

if __name__ == "__main__":

    while(True):
        MenuSYR()
            
        
        
