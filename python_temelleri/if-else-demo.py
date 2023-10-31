import datetime
# ad=input("Ad giriniz:")
# yas=int(input("Yaş giriniz:"))
# egitim=input("Eğitim durumu:")
# if (yas>=18):
#     if (egitim=="lise" or egitim=="üniversite"):
#         print(f"Adınız:{ad}. Ehliyet alabilirsiniz.")
#     else:
#         print("Ehliyet alamazsınız. Eğitim durumunuz yetersiz.")
# else:
#     print(f"Adınız:{ad}. Ehliyet alamazsınız. Yaşınız tutmuyor.")


# not1=float(input("1. yazılı notu giriniz:"))
# not2=float(input("2. yazılı notu giriniz:"))
# sozlu=float(input("Sözlü notunu giriniz:"))
# ortalama=(not1+not2+sozlu)/3
# if ortalama>=0 and ortalama<=24:
#     print(f"Öğrencinin ortalaması:{ortalama}=0")
# elif ortalama>=25 and ortalama<=44:
#     print(f"Öğrencinin ortalaması:{ortalama}=1")    
# elif ortalama>=45 and ortalama<=54:
#     print(f"Öğrencinin ortalaması:{ortalama}=2")
# elif ortalama>=55 and ortalama<=69:
#     print(f"Öğrencinin ortalaması:{ortalama}=3")    
# elif ortalama>=70 and ortalama<=84:
#     print(f"Öğrencinin ortalaması:{ortalama}=4")
# elif ortalama>=85 and ortalama<=100:
#     print(f"Öğrencinin ortalaması:{ortalama}=5")
# else:
#     print("Yanlış bilgi girdiniz!")
# days=int(input("Aracınız kaç gündür trafikte?:"))
# if days<=365:
#     print("1. servis aralığı.")
# elif days>365 and days<= 365*2:
#     print("2. servis aralığı")
# elif days>365*2 and days<=365*3:
#     print("3. servis aralığı")
# else:
#     print("Hatalı süre bilgisi!")
tarih=input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9):")
tarih=tarih.split("/")
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])
trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days
if days<=365:
    print("1. servis aralığı.")
elif days>365 and days<= 365*2:
    print("2. servis aralığı")
elif days>365*2 and days<=365*3:
    print("3. servis aralığı")
else:
    print("Hatalı süre bilgisi!")
