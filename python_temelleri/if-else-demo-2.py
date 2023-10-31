# sayi=float(input("Sayıyı giriniz:"))
# if sayi>0 and sayi<=100:
#     print("Sayı 0 ile 100 arasındadır.")
# else:
#     print("Sayı 0 ile 100 arasında değildir.")

# sayi=int(input("Sayıyı giriniz:"))
# if sayi>0:
#     if sayi%2==0:
#         print("Sayı pozitif çift sayıdır.")  
#     else:
#         print("Sayı pozitif tek sayıdır.")
# elif sayi==0:
#     print("Sayı nötr.")
# else:
#     print("Girilen sayı negatif.")

# email="mert@gmail.com"
# password="abc321"
# girilenEmail=input("Email:")
# girilenPassword=input("Şifre:")
# if girilenEmail==email:
#     if girilenPassword==password:
#         print("Giriş başarılı.")
#     else:
#         print("Girilen şifre yanlış!")
# else:
#     print("Email hatalı!")

# sayi1=int(input("1. Sayı:"))
# sayi2=int(input("2. Sayı:"))
# sayi3=int(input("3. Sayı:"))
# if sayi1>sayi2 and sayi1> sayi3:
#     print(f"Girilen sayılardan en büyüğü 1. sayı={sayi1}")
# elif sayi2>sayi1 and sayi2>sayi3:
#     print(f"Girilen sayılardan en büyüğü 2. sayı={sayi2}")
# elif sayi3>sayi1 and sayi3>sayi2:
#     print(f"Girilen sayılardan en büyüğü 3. sayı={sayi3}")
# else:
#     print("Girilen sayılar eşit.")

# vize1=float(input("1. vize:"))
# vize2=float(input("2. vize:"))
# final=float(input("Final:"))
# ortalama=((vize1+vize2)/2)*0.6 + (final*0.4)

# if ortalama>=50:
#     if final>=50:
#         print(f"Ortalama={ortalama} Geçti.")
#     else:
#         print("Geçme durumu:Başarısız. Final notu 50'den düşük.")
# else:
#     print(f"Ortalama={ortalama} Kaldı.")
# vize1=float(input("1. vize:"))
# vize2=float(input("2. vize:"))
# final=float(input("Final:"))
# ortalama=((vize1+vize2)/2)*0.6 + (final*0.4)

# if ortalama>=50:
#     print("Geçti")
# else:
#     if final>=70:
#         print("Final notu ile geçti.")
#     else:
#         print("Başarısız")

name=input("Adınız:")
kg=float(input("Kilo:"))
hg=float(input("Boy:"))
index=(kg)/(hg**2)
if index>0 and index<=18.4:
    print("Zayıf")
elif index>18.5 and index<=24.9:
    print("Normal")
elif index>25 and index<=29.9:
    print("Kilolu")
elif index>30 and index<=34.9:
    print("Obez")
else:
    print("Hatalı giriş.")



    