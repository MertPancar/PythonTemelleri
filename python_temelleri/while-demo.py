# #1
# sayilar=[1,3,5,7,9,12,19,21]
# i=0
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i+=1
# #2
# baslangic=int(input("Başlangıç değeri:"))
# bitis=int(input("Bitiş değeri:"))
# i=baslangic
# while i<bitis:
#     i+=1
#     if i%2!=0:
#       print(i)
# #3
# i=100
# while i>0:
#     print(i)
#     i-=1

# #4
# numbers=[]
# i=0
# while i<5:
#     sayigir=int(input("Sayıyı giriniz:"))
#     numbers.append(sayigir)
#     i+=1
# numbers.sort()
# print(numbers)

# #5
urunler=[]
i=0
adet=int(input("kaç adet ürün ekliceksiniz:"))
while i<adet:
    name=input("Urun ismi")
    price=input("ürün fiyatı")
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
for urun in urunler:
    print(f"ürün adı:{urun['name']} fiyatı {urun['price']}")