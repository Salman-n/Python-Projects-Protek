def faktorial(n):
    if n<=1:
        return 1
    else:
        return n * faktorial(n-1)
    

def faktorial1(c,d):
    proses = faktorial(c) // (faktorial(d) * faktorial(c-d))
    print('C','(',c,d,')','=', proses)
def faktorial2(c,d):
    proses = faktorial(c) // faktorial(c-d)
    print('P','(',c,d,')','=', proses)

c,d = 5,3
e,f= 10,7
faktorial1(5,3)
faktorial2(10,7)
