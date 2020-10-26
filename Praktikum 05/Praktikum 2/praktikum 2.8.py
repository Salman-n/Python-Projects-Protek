from random import randint
jumRandom = 0
while True:
    
    jumRandom = jumRandom + 1
    
    bil = randint(0, 10)
    print(bil)
    if (bil == 5):
        break

print("Jumlah Perulangan : ", jumRandom)


