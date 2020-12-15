import random
n = (int(input("berapa kali acak ? :")))
x = (input("masukan kata : "))
def shuff(x,n):
    val = x
    daftaracak = []
    for indi in range(n):
        x = list(val)
        random.shuffle(x)
        res = ("".join(x))
        if res not in daftaracak:
            daftaracak.append(res)
        print([res],end ="")
shuff(x,n)
