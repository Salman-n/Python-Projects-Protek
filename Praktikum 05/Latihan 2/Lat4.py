kolom = 5
baris = 5

i = 0 
while (i < kolom):
    j = 1
    while (baris - j >= i):
        print('*', end='')
        j += 1
    print('')
    i += 1
