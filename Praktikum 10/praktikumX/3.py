def program():
    file1 = open('2.txt', 'r') 
    
    Lines = file1.readlines() 
    
    char = {
        1:'a',
        2:'b',
        3:'c',
        4:'d',
        5:'e',
        6:'f',
        7:'g',
        8:'h',
        9:'i',
        10:'j',
        11:'k',
        12:'l',
        13:'m',
        14:'n',
        15:'o',
        16:'p',
        17:'q',
        18:'r',
        19:'s',
        20:'t',
        21:'u',
        22:'v',
        23:'w',
        24:'x',
        25:'y',
        26:'z',
    }
    
    data = {}
    # Strips Garis karakter baru
    y = 0
    for line in Lines: 
        y = y + 1
        x = line.strip().split("|",3)
        dict = {}
        dict["nim"] = x[1]
        dict["nama"] = x[2].replace("\t","")
        dict["alamat"] = x[3]
        data[char[y]] = dict
        
    print(data)
program()
