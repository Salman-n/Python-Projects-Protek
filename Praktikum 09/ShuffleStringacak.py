import random
n = (int(input("berapa kali acak ? :")))
def shuff(n):
    val = "acuk"
    daftaracak = []
    for indi in range(n):
        x = list(val)
        random.shuffle(x)
        res = "".join(x)
        if res not in daftaracak:
            daftaracak.append(res)
        print(res)
shuff(n)
