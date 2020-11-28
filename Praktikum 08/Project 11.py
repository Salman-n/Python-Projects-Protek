#siapkan data buku dalam list
DaftarBuahBuahan = {
    "apel" : 5000,
    "jeruk" : 8500,
    "mangga" : 7800,
    "duku" :6500
}

def spawn(): #fungsi awal program dijalankan
    print("-"*20)
    print("A. Tambah Buku")
    print("B. Beli Buku")
    print("C. Tampilkan List Buah")
    print("D. Exit")
    print()
    selectMenu();
    
    
def selectMenu():
    pilih = input("Pilih Menu: ")

    #jika pilih menu 1
    if pilih == 'A':
        TambahData()
    if pilih == 'B':
        BeliBuah()
    if pilih == 'C':
        TampilBu()
    if pilih == 'D':
        print("Terimakasih sudah menggunakan program ")
        exit()
        selectMenu()
    
def TambahData():
    print("Input Buku Baru")
    print("="*20)
    judul = input("Masukan Nama Buah  : ")
    harga = input("Masukan Harga Buah : ")
    print("-"*20)
    hargaint = 0
    try:
        harga = int(harga)
    except:
        input("Terjadi kesalahan! pastikan hanya menginput angka saat diminta mengisi harga\nTekan enter untuk mengulangi proses input")
        tambahBuku()
    DaftarBuahBuahan[judul] = hargaint;
    input("Buah " + judul + " Berhasil di input . tekan Enter untuk kembali")
    print(DaftarBuahBuahan)
    spawn();

def BeliBuah():
    TotalHarga= 0
    while True :
        memilih = input("Nama buah yang dibeli  = ")
        if  memilih in DaftarBuahBuahan :
            masukanBerat = int(input("Silahkan Masukan Total Buah yang akan anda beli : "))
            print("Total buah yang akan di beli (Kg) :", masukanBerat,"Kg")
            print("="*50)
            inpPilihan = str(input("Beli buah yang lain (y/n) ?  = "))
            TotalHarga += (DaftarBuahBuahan[memilih]*masukanBerat)
            if inpPilihan == "y":
                continue
            if inpPilihan == "n":
                print("Total harga           : Rp.",TotalHarga)
                break
        else :
            print("Nama Buah tidak terdaftar")
        break        
    spawn()

def TampilBu():
    print("Daftar Buah yang tersedia")
    print("="*20)
    nobuah = 1
    for key, val in DaftarBuahBuahan.items():
      print("[" + str(nobuah)+ '] ' + key + " (Rp " + str(val) +")")
      nobuah +=1 
    print("-"*20)
    input("Tekan Enter untuk kembali")
    spawn()

spawn();

