Data = []
inpBuah = int(input("Masukan jumlah buah : "))
def sortStringByChar(Data):
    angkaBuah = 0
while True :
    for angkaBuah in range (0, inpBuah):
            angkaBuah += 1
            posisiKe = str(input("Masukan Nama Buah ke-" + str(angkaBuah) + " = "))
            Data.append(posisiKe)
            if angkaBuah == inpBuah:
                print(Data)
                print("")
                break
            continue
    print("")
    print("------------------------------")
    print("Hasil Sort Data Buah : ")
    Data.sort(key = len, reverse = True)
    print(Data)
    sortStringByChar(Data)
    print("------------------------------")
    break
    
