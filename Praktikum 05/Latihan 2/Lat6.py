import random 
rentangAngka = random.randint(0,100)
print("---------------Game Tebak Angka Mr.Sekuyy---------------")
print("Hai.. nama saya Mr. Sekuyy, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!! semoga beruntung")
print("--------------------------------------------------------")
nama = str(input("isi nama Anda =>"))
skornya = 100
while True :
    Tebaklah = int(input("Tebakan Anda => "))
    if (Tebaklah == rentangAngka):
        print("wadidaw...Bilangan Tebakan Anda Benar, yoww", Tebaklah)
        print("Selamat" ,nama, "telah berhasil menebak angka")
        break
        end()
    elif (Tebaklah < 0):
        print("Angka tidak masuk rentang 0 - 100", Tebaklah)
    elif (Tebaklah > rentangAngka) :
        print("wow...Bilangan Tebakan Anda Terlalu besar, broww", Tebaklah)
        skornya -=2
    elif (Tebaklah < rentangAngka ):
        print("waduhh..Bilangan Tebakan Anda Terlalu kecil, broww", Tebaklah)
        skornya -=2

print("Score",nama,"adalah", skornya)
    
       
