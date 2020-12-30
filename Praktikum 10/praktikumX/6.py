def encrypt(text,s):
 hasil = ""
 for i in range(len(text)):
      char = text[i]
      if char != ' ':
          if (char.isupper()):
             hasil += chr((ord(char) + s-65) % 26 + 65)
          else:
             hasil += chr((ord(char) + s - 97) % 26 + 97)
      else:
          hasil += " "
 return hasil
 
s = int(input("Masukan n Sandi Caesar : "))

text = "SAYA SUKA PYTHON"

teks = encrypt(text,s)
print(teks)

# buka file untuk ditulis
Bukafile = open('6.txt', 'a')
# tulis teks ke file
Bukafile.write(teks)
Bukafile.seek(0, 0)
# tutup file
Bukafile.close()
