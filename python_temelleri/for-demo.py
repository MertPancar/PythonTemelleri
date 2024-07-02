#1
sayilar=[1,3,5,7,9,12,19,21]
ucunkatlari=[]
# for uckati in sayilar:
#     if uckati%3==0:
#         ucunkatlari.append(uckati)
# print(ucunkatlari)
#2
toplam=0
for sayi in sayilar:
    toplam+=sayi
print(toplam)
#3
teksayilarinkaresi=[]
for teksayi in sayilar:
    if teksayi%2==1:
        teksayilarinkaresi.append(teksayi**2)
print(teksayilarinkaresi)
#4
enfazla5karakterlisehirler=[]
sehirler=['Kocaeli','İstanbul','Ankara','İzmir','Rize']
for sehir in sehirler:
    if len(sehir)<=5:
        enfazla5karakterlisehirler.append(sehir)
print(enfazla5karakterlisehirler)
#5
urunler=[
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
]
urunlerintoplamı=[]
fiyattoplam=0
for urun in urunler:
    fiyattoplam+=int(urun['price'])
print(fiyattoplam)
#6
for urun in urunler:
    if(int(urun['price'])<=5000):
        print(urun['name'])



    

