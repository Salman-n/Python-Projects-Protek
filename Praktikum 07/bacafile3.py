file = open("d:/data2.txt", "r")
def bacafile3():
    file = open("d:/data2.txt", "r")
try:
    sum = 0
    for data in file:
        sum = sum + int(data)
        print(sum)
except ValueError:
    print("Input Terjadi kesalahan")
    pass

