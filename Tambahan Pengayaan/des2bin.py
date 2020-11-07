n = int(input("Silahkan Masukan bilangan / angka yang anda mau: "))
binary = ''
rem = 0
def Dec2bin(n):
    
    while True:
    
        rem = n % 2
        if n > 1:
            Dec2bin(n // 2)
        print(rem, end= '')
        binary = str(rem) + binary
        
print("<<-------------------------->>")      
print("Konversi ke binernya: ", binary)

def Dec2bin(n):    
    if n > 1: 
        Dec2bin(n // 2) 
    print(n % 2, end = '') 
if __name__ == "__main__": 
    des = n
    Dec2bin(des) 
