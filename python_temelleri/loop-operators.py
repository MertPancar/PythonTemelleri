# for item in range(100,150,10):
#     print(item)
# print(list(range(100,150,10)))

# greetings='Hello'
# for index,item in enumerate(greetings):
#     print(f'index:{index} letter:{item}')
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]
# print(list(zip(list1,list2,list3)))
for a,b,c in zip(list1,list2,list3):
    print(a,b)
   