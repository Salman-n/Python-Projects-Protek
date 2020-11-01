def summarize(*semuaAngka):
    jumlahKeseluruhan = 0
    for angka in semuaAngka:
        jumlahKeseluruhan = jumlahKeseluruhan + angka
    return jumlahKeseluruhan

def average(*semuaAngka):
    hitung = 0
    for angka in semuaAngka:
        hitung = hitung + 1
    jumlahKeseluruhan = summarize(*semuaAngka) / hitung
    return jumlahKeseluruhan

def maks(*semuaAngka):
    dataTerbesar = semuaAngka[0]
    for angka in semuaAngka:
        if not dataTerbesar:
            dataTerbesar = angka
        if(angka > dataTerbesar):
            dataTerbesar = angka
    hasilnya = dataTerbesar
    return hasilnya

def min(*semuaAngka):
    dataTerkecil = semuaAngka[0]
    for angka in semuaAngka:
        if not dataTerkecil:
            dataTerkecil = angka
        elif(angka < dataTerkecil):
            dataTerkecil = angka
    hasilnya = dataTerkecil
    return hasilnya
    
    
    
        
    

