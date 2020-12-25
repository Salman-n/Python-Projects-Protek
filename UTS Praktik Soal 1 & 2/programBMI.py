print('<<','-'*30,"Program BMI UTS soal ke-1",'-'*30,'>>')
print("\n   Selamat Datang di program BMI, untuk mengetahui status Berat Badan Anda"  )
print('<<','-'*90,'>>')
inpTinggi = int(input("\n  Silahkan Masukan Input Tinggi badan anda :" ))
""" Maksudnya In1 adalah input kedua inpTinggi, karena harus diubah tinggi menjadi m untuk dihitung dalam rumus BMI """
In1 = inpTinggi * 0.01
inpBerat  = int(input("\n  Silahkan Masukan Input Berat badan anda  :" ))
print('\n')


def pengukurStatusBMI(In1, inpBerat):
    """Rumus BMI = Berat badan(kg) dibagi Tinggi badan(cm)""" 
    pengukurStatusBMI = inpBerat // (In1 * In1)
    if(pengukurStatusBMI < 18):
        print(" Statusnya adalah KURUS ")
    elif(pengukurStatusBMI >= 18 and pengukurStatusBMI < 23):
        print(" Statusnya adalah IDEAL ")
    elif(pengukurStatusBMI >= 23 and pengukurStatusBMI < 27):
        print(" Statusnya adalah GEMUK ")
    elif(pengukurStatusBMI >= 27 and pengukurStatusBMI < 35):
        print(" Statusnya adalah OBESITAS ")
    elif(pengukurStatusBMI >= 35):
        print(" Statusnya adalah OBESITAS MORBID ")
        
Output = inpBerat /(In1 * In1)

print('>>','-'*25,"Hasil Program BMI",'-'*28,'<<')
print(" input anda :")
print(" Tinggi Badan anda    : ",inpTinggi,"cm")
print(" Berat Badan anda     : ",inpBerat,"Kg")
print(" BMI anda             : ",Output)
pengukurStatusBMI(In1, inpBerat)
