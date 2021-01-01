from datetime import date
import datetime

denda = 2000

def cari(query):
	file1 = open('DaftarPeminjam.txt', 'r') 
	Lines = file1.readlines()
	teks=""
	ditemukan = False	
	kodemember = ""
	namamember = ""
	judulbuku = ""
	
	tgl_start = date.today();	
	tgl_end = date.today()
	tgl_pengembalian = date.today();

	for line in Lines:
		x =line.strip().split("|",5);
		if query == x[1]:
			ditemukan = True
			kodemember = x[1]
			namamember = x[2]
			judulbuku = x[3]
			tgl_start = datetime.datetime.strptime(x[4], '%Y-%m-%d').date()
			tgl_end = datetime.datetime.strptime(x[5], '%Y-%m-%d').date()
			break

	if ditemukan == True:
		telat = (date.today() - tgl_end).days;
		totaldenda = 0
		if telat > 0:
			totaldenda = denda * telat

		print("Data Peminjaman Buku")
		print("Kode Member : " + kodemember)
		print("Nama Member : " + namamember)
		print(" ")
		print("Judul Buku : "+judulbuku)
		print("Tanggal Mulai Peminjaman : " + str(tgl_start))
		print("Tanggal Maks Peminjaman : " + str(tgl_end))
		print("Tanggal Pengembalian : " + str(tgl_pengembalian))
		print("Terlambat : " + str(telat))
		print("Denda : Rp " + str(totaldenda))
	else:
		print("Member Tidak Ditemukan")


cari(str(input("Masukan Kode Member : ")))
