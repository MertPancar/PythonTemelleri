girilensayi=int(input("Sayı giriniz:"))
asalmi=True
if girilensayi==1:
    asalmi=False
for i in range(2,girilensayi):
    if(girilensayi%i==0):
        asalmi=False
        break
if asalmi:
    print("Sayı asaldır.")
else:
    print("Asal değildir.")