# ogrenciler={
#     "120":{

#         "ad":"Ali",
#         "soyad":"Yılmaz",
#         "telefon":"0123456789"
#     },
#     "125":{

#         "ad":"Can",
#         "soyad":"Korkmaz",
#         "telefon":"9876543210"
#     },
#     "128":{

#         "ad":"Volkan",
#         "soyad":"Yükselen",
#         "telefon":"7891011120"
#     }
    
#     }
ogrenciler={}
number=input("ogrenci no giriniz:")
name=input("ogrenci ad giriniz:")
surname=input("ogrenci soyad giriniz:")
phone=input("ogrenci telefon giriniz:")

# ogrenciler[number]={
#     "ad":name,
#     "soyad":surname,
#     "telefon":phone
# }

ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

number=input("ogrenci no giriniz:")
name=input("ogrenci ad giriniz:")
surname=input("ogrenci soyad giriniz:")
phone=input("ogrenci telefon giriniz:")
ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

number=input("ogrenci no giriniz:")
name=input("ogrenci ad giriniz:")
surname=input("ogrenci soyad giriniz:")
phone=input("ogrenci telefon giriniz:")

ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})
print("*"*50)
print(ogrenciler)
ogrNo=input("Öğrenci No:")
ogrenci=ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")

# print(ogrenciler["128"])