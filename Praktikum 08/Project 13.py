def nilaiMaksimal(DataNilai):
        bilMaks = 0
        dataDictinya = {}
        for data in DataNilai:
                    nilaiuas = data.get("uas")
                    nilaimid = data.get("mid")
                    methodRumusHitung =  (nilaimid + nilaiuas*2 )/3
                    if(methodRumusHitung > bilMaks):
                        bilMaks = methodRumusHitung
                        dataDictinya["nim"]  = data.get("nim")
                        dataDictinya["nama"] = data.get("nama")

        print("Nilai akhir tertinggi diperoleh mahasiswa ",dataDictinya["nama"] ,"dengan NIM",dataDictinya["nim"])
print("="*50)
DataNilai = [{'nim' : 'A01','nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Aku',  'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

nilaiMaksimal(DataNilai)


