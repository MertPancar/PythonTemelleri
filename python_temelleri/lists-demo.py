arabamarkalari=["Bmw","Mercedes","Opel","Mazda"]
# ekstra=["Audi","Nissan"]
# arabamarkalari.extend(ekstra)
# arabamarkalari.pop(5)
# arabamarkalari.reverse()
result="Merceddes" in arabamarkalari
result=arabamarkalari[-2]
result=arabamarkalari[0:3]
arabamarkalari[-2:]=["Toyota","Reneault"]
result=arabamarkalari+["Audi","Nissan"]
del arabamarkalari[0]
result=arabamarkalari
result=arabamarkalari[::-1]
# print(arabamarkalari)
# # print(len(arabamarkalari))
# # print(arabamarkalari[0],arabamarkalari[1],arabamarkalari[2])
studentA=["Yiğit","Bilgi",2010,[70,60,70]]
studentB=["Sena","Turan",1999,[80,80,70]]
studentC=["Ahmet","Turan",1998,[80,70,90]]
ogrencilist=[studentA,studentB,studentC]
# result=studentB[3][1]
# result=studentA[0]
# result=studentC[2]
result=f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {round((studentA[3][0]+studentA[3][1]+studentA[3][2])/3, 2)}"
print(result)
print(ogrencilist)
print(arabamarkalari)

