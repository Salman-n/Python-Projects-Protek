masukan = int(input("Silahkan masukan angka biner yang anda mau: "))
print('---------------------------------------')
def bin2des(s):
    biner = s
    desi  = 0
    j = 0
    while(s != 0):
        hasilbagi = s % 10
        desi += hasilbagi * pow(2, j)
        s = s//10
        j = j + 1
    print('Konversi ke Desimalnya :',biner,'==>',desi)

if __name__ == '__main__':
   bin2des(masukan)
