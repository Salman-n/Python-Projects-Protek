def decrypt(message,key):
       LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
       key = key
       translated = ''
       for symbol in message:
          if symbol in LETTERS:
             num = LETTERS.find(symbol)
             num = num - key
             if num < 0:
                num = num + len(LETTERS)
             translated = translated + LETTERS[num]
          else:
             translated = translated + symbol
       return translated


file1 = open('6.txt', 'r') 
Lines = file1.readlines()
teks=""
for line in Lines:
    teks = line.strip()

s = int(input("Masukan n Sandi Caesar : "))
print(decrypt(teks,s))
