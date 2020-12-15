import random
n = (int(input("berapa kali acak ? :")))
def shuff(n):
    val = (input("masukan kata yang ingin diacak ?: "))
    daftaracak = []
    for indi in range(n):
        x = list(val)
        random.shuffle(x)
        res = "".join(x)
        if res not in daftaracak:
            daftaracak.append(res)
        print([res])
        print("-"* 25)

shuff(n)
