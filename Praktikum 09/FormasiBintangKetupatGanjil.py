x = int(input("Masukan nilai n bintang formasi :"))
print("")
def formasi1(x):
     for y in range(x):
       if y % 2 != 1:
         y = y+1;
         print( ("*"*y).center(1+2*x) )

     for y in reversed(range(x)):
       if y % 2 == 1:
         y = y;
         print( ("*"*y).center(1+2*x ) )
formasi1(x)
