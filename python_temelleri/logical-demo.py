#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol et.

# x=float(input("Sayıyı giriniz:"))
# result=(x>0) and (x<=100)
# print(f"Girilen sayının 0 ile 100 arasında olma durumu:{result}")

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol et.

# x=int(input("Sayıyı giriniz:"))
# result=(x>0) and (x%2==0)
# print(f"Girilen sayının pozitif ve çift sayı olma durumu:{result}")

#3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email="mert@gmail.com"
# password="abc123"
# girilenEmail=input("Email:")
# girilenPassword=input("Parola:")
# giriskontrol=(email==girilenEmail) and (password==girilenPassword)
# print(f"Giriş başarılı olma durumu:{giriskontrol}")

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
# result=(a>b) and (a>c)
# print(f"a en büyük sayı mı:{result}")
# result=(b>a) and (b>c)
# print(f"b en büyük sayı mı:{result}")
# result=(c>b) and (c>a)
# print(f"c en büyük sayı mı:{result}")

# vize1=float(input("Vize 1 notu giriniz:"))
# vize2=float(input("Vize 2 notu giriniz:"))
# final=float(input("Final notu giriniz:"))
# ortalama=((vize1+vize2)/2)*0.6+(final*0.4)
# # result=(ortalama>=50) and (final>=50)
# result=(ortalama>=50) or (final>=70)
# print(f"Öğrencinin not ortalaması:{ortalama} ve dersten geçme durumu:{result}")

name=input("Adınız:")
kg=float(input("Kilo girin:"))
hg=float(input("Boy girin:"))
index=(kg)/(hg**2)
zayif=(index>=0) and (index<=18.4)
normal=(index>18.4) and (index<=24.9)
kilolu=(index>24.9) and (index<=29.9)
obez=(index>29.9) and (index<=34.9)

print(f"{name} kilo indeksi:{index} ve kilo değerlendirmen zayıf:{zayif}")
print(f"{name} kilo indeksi:{index} ve kilo değerlendirmen normal:{normal}")
print(f"{name} kilo indeksi:{index} ve kilo değerlendirmen kilolu:{kilolu}")
print(f"{name} kilo indeksi:{index} ve kilo değerlendirmen obez:{obez}")



