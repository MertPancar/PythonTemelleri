users={
    "Mert Karabacak":{
    "age":22,
    "roles":["user"],
    "email":"mert@mail.com",
    "adres":"türkiye",
    "phone":"9876543210"
},
    "mahmut taş":{
    "age":55,
    "roles":["admin","user"],
    "email":"mahmut@mail.com",
    "adres":"avrupa",
    "phone":"1234567890"
    }
}
print(users["mahmut taş"]["roles"][0])