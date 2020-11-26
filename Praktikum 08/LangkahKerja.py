print(">"*46)
print("")
print("Membuat List A dan B")
print("")
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print("List A =", a)
print("List B =", b)
print("")


print("-"*46)
print("")
print("Menyisipkan nilai kedalam Indeks A dan B")
print("")
a.insert(3, 10)
b.insert(2, 15)
print("Hasil setelah menyisipkan nilai 10 dalam indeks 3 =", a)
print("Hasil setelah menyisipkan nilai 15 dalam indeks 2 =", b)
print("")


print("-"*46)
print("")
print("Menyisipkan nilai kedalam indeks terakhir")
print("")
a.append(4)
b.append(8)
print(a)
print(b)
print("")


print("-"*46)
print("")
print("Melakukan Sorting Ascending (reverse = False)")
print("")
a.sort(reverse = False)
b.sort(reverse = False)
print(a)
print(b)
print("")


print("-"*46)
print("")
print("Membuat list baru dari hasil sublist a dan b")
print("")
c = a[0:8]
d = b[2:10]
print(c)
print(d)
print("")


print("-"*46)
print("")
print("Membuat list baru dari penjumlahan list a + b")
print("")
e = []
isi = 0
for isi in range(len(c)):
        hasil = c[isi] + d[isi]
        e.append(hasil)
print(e)
print("")


print("-"*46)
print("")
print("Mengubah list jadi tuple")
print("")
E = tuple(e)
print(E)
print("")

print("-"*46)
print("")
print("Mencari nilai maks, min, jumlah keseluruhan nilai dari list e")
print("")
e = [6, 8, 10, 12, 13, 14, 18, 22]
Totalnilai = 0
nilaiTerbesar = [0]
nilaiTerkecil = [0]
for nilai in e:
    Totalnilai = Totalnilai + nilai    
    if nilaiTerbesar: 
        nilaiTerbesar = max(e)
    if nilaiTerkecil:
        nilaiTerkecil = min(e)
print("Nilai Terbesar dari list e ialah", nilaiTerbesar)
print("Nilai Terkecil dari list e ialah", nilaiTerkecil)
print("Total Nilai dari list e ialah", Totalnilai)
print("")


print("-"*46)
print("")
print("Membuat sebuah string")
print("")
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(str(myString))
print("")


print("-"*46)
print("")
print("Menggunakan set() dalam menyusun huruf dari sebuah string")
print("")
hrfTerpisah = set(myString)
print(hrfTerpisah)
print("")


print("-"*46)
print("")
print("mengubah ke list")
print("")
ubhKeList = list(hrfTerpisah)
print(ubhKeList)
print("")


print("-"*46)
print("")
print("mengurut secara alpabet")
print("")
ubhKeList.sort(reverse = False)
print(ubhKeList)
print("")
print("<"*46)

