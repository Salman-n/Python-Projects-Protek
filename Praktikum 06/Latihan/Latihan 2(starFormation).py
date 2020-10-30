def starFormation1(n):
 for b in range (0,n):
    for bn in range (0,n):
        if bn>b:
            print()
            break
        else:
            print("*",end="")
 
starFormation1(4)
print()
print()

def starFormation2(n):
 for b in range (0,n):
    for bn in range (0,n-b):
         print('*', end='')
    print()
    
starFormation2(4)
print()
print()

def starFormation3(n):
 for b in range((n+1)//2):
    for bn in range(b+1):
        print('*' , end='')
    print('')
 
 for b in reversed(range(((n+1)//2) - 1)):
    for bn in range(b+1):
        print('*' , end='')
    print('')
    
starFormation3(7)
print()



