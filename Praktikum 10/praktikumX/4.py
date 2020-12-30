def program():
    file1 = open('2.txt', 'r') 
    
    Lines = file1.readlines() 
    
    query = input("Masukan NIM yang mau dicari: ")
      
    
    data = []
    ketemu = False
    # Strips the newline character 
    
    for line in Lines: 
        x = line.strip().split("|",3)
        if query == x[1]:
            print("Data Mahasiswa: ")
            print("NIM           : " + x[1])
            print("Nama          : " + x[2])
            print("Alamat        : " + x[3])
            ketemu = True
            break
    
    if ketemu == False:
        print("Nim Tidak Ditemukan")
    
program()
