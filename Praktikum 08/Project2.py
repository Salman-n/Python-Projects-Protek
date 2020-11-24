X = [10,12,26,35,46,53,65,4]
C = X[0]
B = X[0]
A = 0
BanyakNomor = 0
TotalJumlah = 0
def dataStat(X):   
        X = [10,12,26,35,46,53,65,4]
        C = X[0]
        B = X[0]
        A = 0
        BanyakNomor = 0
        TotalJumlah = 0
try:
            for nomor in X:
                BanyakNomor += 1
                TotalJumlah += nomor
                if C > nomor:
                  C = nomor
                if B < nomor:
                  B = nomor

            A = TotalJumlah // BanyakNomor
            print("-"*80)
            print('Daftar Nomor                  : ',X)
            print('Jumlah banyak Nomor           : ',BanyakNomor)
            print('Total Jumlah                  : ',TotalJumlah)
            print('rata-rata       (A)           : ',A)
            print('nilai terbesar  (B)           : ',B)
            print('nilai terkecil  (C)           : ',C)
            print("-"*80)
            
except Invalid:
            print("terjadi kesalahan input tidak benar / invalid")

dataStat(X)
