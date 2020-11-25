daftarbuah = {"apel" : [5000], "jeruk" : [8500], "mangga" : [7800], "duku" : [6500]}
def sortBuahTermahal(daftarbuah):
        for harga in sorted(daftarbuah, key=daftarbuah.get, reverse=True):
                print("buah",harga,"dengan harga termahal adalah :", daftarbuah[harga])
                break

sortBuahTermahal(daftarbuah)
