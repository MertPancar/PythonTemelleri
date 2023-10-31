x,y,z=2,5,10
numbers=1,5,7,10,6
# sayi1=input("1. Sayıyı giriniz:")
# sayi2=input("2. Sayıyı giriniz:")
# carpim=int(sayi1)*int(sayi2)
# toplam=x+y+z
# # print(carpim-toplam)
# # bolum=y//x
# # print(bolum)
# mod=toplam%3
# print(mod)
# us=y**x
# print(us)
x,*y,z=numbers
result=y[0]+y[1]+y[2]
print(result)

