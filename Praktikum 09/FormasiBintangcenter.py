x = int(input("Masukan nilai n bintang formasi :"))
print("")
def formasi1(x):
     while True :
          for bintang in range(x):
              print(('*'*(1+2*bintang)).center(1+2*x))
          break
formasi1(x)

