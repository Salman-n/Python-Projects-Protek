filename = "data.txt"
try:
    file = open("c:/data.txt", "r")
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' sama dengan', hasil)
except FileNotFoundError:
    print('Terjadi kesalahan pada path nama file')
    print('tidak ditemukan', filename)
except ZeroDivisionError:
    print('Pembagian tidak boleh dengan angka 0')
try:
    file = open("d:/data.txt", "r")
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' sama dengan', hasil)
except FileNotFoundError:
    print('Terjadi kesalahan pada path nama file')
    print('tidak ditemukan', filename)
except ZeroDivisionError:
    print('Pembagian tidak boleh dengan angka 0')
