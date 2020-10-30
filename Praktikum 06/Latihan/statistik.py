def sum(*semuaAngka):
    jumlahKeseluruhan = 0
    for angka in semuaAngka:
        jumlahKeseluruhan += angka
    return jumlahKeseluruhan

def average(*semuaAngka):
    hitung = 0
    for angka in semuaAngka:
        hitung += 1
    jumlahKeseluruhan = sum(*semuaAngka) / hitung
    return jumlahKeseluruhan

def maks(*semuaAngka):
    dataTerbesar = semuaAngka[0]
    for angka in semuaAngka:
        if(angka > dataTerbesar):
            dataTerbesar = angka
    hasilnya = dataTerbesar
    return hasilnya

def min(*semuaAngka):
    dataTerkecil = semuaAngka[0]
    for angka in semuaAngka:
        if(angka < dataTerkecil):
            dataTerkecil = angka
    hasilnya = dataTerkecil
    return hasilnya
    
    
    
        
    

