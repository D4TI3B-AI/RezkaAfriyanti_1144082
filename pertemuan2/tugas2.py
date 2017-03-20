graph = {'Arcamanik': ['Sukamiskin', 'GedeBage','Antapani','Ujung Berung'],
             'Arcamnik': ['Ujung Berung', 'Antapani','GedeBage','Sukamiskin'],
             'Ujung Berung': ['Arcamanik','Sukamiskin','GedeBage','cileunyi'],
             'GedeBage': ['Arcamanik','Ujung Berung','cileunyi'],
             'Sukamiskin': ['cicahem','Arcamanik','Antapani','UjungBerung'],
             'Antapani': ['KiaraCondong','Sukamiskin','Cicahem'],
             'Cicahem': ['antapani'],
             'KiaraCondong': ['Antapani'],
             'Cileunyi': ['UjungBerung','GedeBage'],
         }
 
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalul kecamatan Kota Bandung")
print ("(Arcamanik,GedeBage,Antapani,Sukamiskin,Ujung Berung)")
print ("(Cileunyi,Cicahem,KiaraCondong)")
print ("\n")
awal = raw_input("Masukan Awal : ")
tujuan = raw_input("Masukan Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
