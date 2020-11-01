def faktorialnya(n):
    """Faktorial buat per angka"""
    fkt={}
    if n in fkt:
        return fkt[n]
    elif n == 0 or n == 1 :
        return 1
        fkt[n] = 1
    else:
        faktorial = n * faktorialnya(n-1)
        fkt[n] = faktorial
    return faktorial
def kombin(c,d):
    proses = faktorialnya(c) // (faktorialnya(d) * faktorialnya(c-d))
    print('C','(',c,d,')','=', proses)
def permut(c,d):
    proses = faktorialnya(c) // faktorialnya(c-d)
    print('P','(',c,d,')','=', proses)
print('-----------------------------------') 
c,d = 5,3
e,f = 10,7
kombin(5,3)
permut(10,7)
