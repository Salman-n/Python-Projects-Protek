bil = []
hsl = []
inputBil = int(input("Silahkan Masukan jumlah Bilangan : "))
def kuadrat(bil):
        angkaBil = 0
while True :
    for angkaBil in range (0,inputBil):
            angkaBil += 1
            angkaKe = int(input("Masukan Angka ke -" + str(angkaBil) + " =>"))
            bil.append(angkaKe)
            if angkaBil == inputBil:
                print(bil)
                break
         
    while hsl != 0:
        for HasilKuadrat in bil :
            hsl.append(HasilKuadrat ** 2)
            print(hsl)
        break
    print("Hasil Perpangkatan Kuadrat dari ", bil, "Adalah :", hsl)
    kuadrat(bil)
    break
    


