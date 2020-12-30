def program():
    file1 = open('1.txt', 'r') 
    
    Lines = file1.readlines() 
    
      
    
    ganjil = 0
    genap = 0
    # Strips the newline character 
    
    for line in Lines: 
    
        angka = int(line.strip())
        if angka % 2 == 1:
            ganjil += 1
        else:
            genap += 1 
    
    print("Jumlah Ganjil : " + str(ganjil) )
    
    print("Jumlah Genap : " + str(genap) )
program()