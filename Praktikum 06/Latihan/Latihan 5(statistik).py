from statistik import*

def hitung(*semuaAngka):
    print("5, 10, 4, 9, 30, 16, 2, 11")
    print("rata-rata       =>",
          average(5, 10, 4, 9, 30, 16, 2, 11))
    print("nilai maksimum  =>",
          maks(5, 10, 4, 9, 30, 16, 2, 11))
    print("nilai minimum   =>",
          min(5, 10, 4, 9, 30, 16, 2, 11))
    print('')
def hitung2(*semuaAngka):
    print("81, 98, 12, 83, 45, 77, 69, 30, 56")
    print("rata-rata       =>",
          average(81, 98, 12, 83, 45, 77, 69, 30, 56))
    print("nilai maksimum  =>",
          maks(81, 98, 12, 83, 45, 77, 69, 30, 56))
    print("nilai minimum   =>",
          min(81, 98, 12, 83, 45, 77, 69, 30, 56))
    
hitung(5, 10, 4, 9, 30, 16, 2, 11)
hitung2(81, 98, 12, 83, 45, 77, 69, 30, 56)
