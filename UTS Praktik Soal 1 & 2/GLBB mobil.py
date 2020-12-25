print("<<","="*15,"Program Jarak Mobil GLBB UTS soal ke-2(Gerak Lurus Berubah Beraturan)","="*15,">>")
print("\n Program ini untuk melihat mobil dalam menempuh laju jarak per detiknya.")
print("\n","="*105)
Vo= int(input("\n Silahkan masukan kecepatan mula-mula sebuah mobil (Vo) = "))
A = int(input(" Silahkan masukan percepatan (A)                        = "))
t = 0
print("="*30)
print('')
def GlbbMobilnya(t,A,Vo):
    t = 0 
    while t < 11:
        t = t+1
        jarak_S= (Vo*t) +(A*(t**2)/2)
        print("t = " ,t,  ",","S(t) = ", jarak_S)
        if t == 10:
            break
GlbbMobilnya(t,A,Vo)
print('')
print("="*30)
