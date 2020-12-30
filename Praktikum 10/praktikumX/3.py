def program():
    file1 = open('2.txt', 'r') 
    
    Lines = file1.readlines() 
    
      
    
    data = []
    # Strips the newline character 
    
    for line in Lines: 
        x = line.strip().split("|",3)
        dict = {}
        dict["nim"] = x[1]
        dict["nama"] = x[2].replace("\t","")
        dict["alamat"] = x[3]
        data.append(dict)
        
    print(data)
program()
