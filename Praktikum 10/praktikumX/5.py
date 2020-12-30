def program():
    file1 = open('5.txt', 'r') 
    
    Lines = file1.readlines() 
    
      
    
    data = []
    # Strips the newline character 
    
    for line in Lines: 
        x = line.strip().split("|",2)
        hasil = int(x[1]) + int(x[0])
        print(str(hasil))
    
program()
