import random
n = (int(input("berapa kali acak ? :")))
x = (input("masukan kata : "))
def shuff(x,n):
    val = x
    daftaracak = []
    x = list(val)
    for indi in range(n):
        random.shuffle(x)
        res = ("".join(x))
        if res not in daftaracak:
            daftaracak.append(res)
    print(daftaracak,end ="")
shuff(x,n)
