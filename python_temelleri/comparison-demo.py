#1- Girilen 2 sayıdan hangisi büyüktür?
# a=int(input("1. sayıyı giriniz:"))
# b=int(input("2. sayıyı giriniz:"))
# result=(a>b)
# print(f"a:{a} b:{b} den büyüktür:{result}")

#2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize1=float(input("Vize 1 notu giriniz:"))
# vize2=float(input("Vize 2 notu giriniz:"))
# final=float(input("Final notu giriniz:"))
# ortalama=(((vize1+vize2/2))*0.6)+(final*0.4)
# print(f"Not ortalamanız:{ortalama} ve dersten geçme durumunuz {ortalama>=50}")

#3- Girilen bir sayının tek mi çift mi olduğunu yazdırın

# sayi=int(input("Sayıyı girin:"))
# result=(sayi%2==0)
# print(f"Gİrilen sayı çift olma durumu:{result}")

#4- Girilen sayının negatif mi pozitif mi olduğunu yazdırın

# sayi=int(input("Sayıyı girin:"))
# result=(sayi>0)
# print(f"Girilen sayının pozitif olma durumu:{result}")

#5- Parola ve Email bilgisini isteyip doğruluğunu kontrol ediniz

email="mert@gmail.com"
password="abc123"
girilenEmail=input("email:")
girilenPassword=input("parola:")
isEmail=(email==girilenEmail)
isPassword=(password==girilenPassword)
print(f"Email bilgisi doğru mu?:{isEmail} ve parola doğru mu?:{isPassword}")



