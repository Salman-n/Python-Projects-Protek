filename = "myfile.txt"
print ("================ diatas jika penagalamatan Path salah ===============")
def bacafile():
    filename = "myfile.txt"
try:
    file = open("c:/myfile.txt", "r")
    print(file.read())
except :
    print("kesalahan pada path nama file")
    print('tidak ditemukan', filename)

print("")
print ("================ dibawah jika pengalamatan Path file benar ===============")
try:
    file = open("d:\Python Projects Protek\Python-Projects-Protek\Praktikum 07\myfile.txt", "r")
    print(file.read())
except :
    print("kesalahan pada path nama file")
    print('tidak ditemukan', filename)
