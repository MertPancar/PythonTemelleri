def sayHello(name='user'):
    return 'Hello '+name
msg=sayHello('Mert')
print(msg)

def total(num1,num2):
    return num1+num2 
result=total(41588,526569)
print(result)

def yasHesapla(dogumYili):
    return 2024-dogumYili
yas1=yasHesapla(2002)
print(yas1)

def EmekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı.
    INPUT: Doğum yılı.
    OUTPUT: Hesaplanan yıl bilgisi.
    '''
    yas=yasHesapla(dogumYili)
    emeklilik= 65-yas
    if emeklilik>0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz.')
EmekliligeKacYilKaldi(2002,'Mert')
help(EmekliligeKacYilKaldi)
list=[1,2,3]
print(help(list.append))