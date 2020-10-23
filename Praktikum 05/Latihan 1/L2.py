bIndo = int(input("masukan nilai Bahasa Indonesia => "))
MTK   = int(input("masukan nilai Matematika => "))
IPA   = int(input("masukan nilai IPA => "))

print("+++++++++++++++++++++++++++++++++++++++++++++++++")
if ((bIndo > 100) or (bIndo < 0) or (MTK > 100) or (MTK < 0) or (IPA > 100) or (IPA < 0)):
    status = "Maaf, Input Ada Yang Tidak Valid"
    print("Status Kelulusan: {0}".format(status))
elif ((bIndo >= 60) and (bIndo <= 100)and(MTK >= 70) and (MTK <= 100) and (IPA >= 60) and (IPA <= 100)):
    status = "Lulus"
    print("Status Kelulusan: {0}".format(status))
elif ((bIndo >= 0) or (bIndo < 60) or (MTK >= 0) or (MTK < 70) or (IPA >= 0) or (IPA < 60)):
    status = "Tidak Lulus"
    print("Status Kelulusan => {0}".format(status))
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
