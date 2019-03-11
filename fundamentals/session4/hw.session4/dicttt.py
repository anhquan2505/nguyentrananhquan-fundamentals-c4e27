inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket']=['seashell', 'strange berry','lint']


inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory)



price ={
    "banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock= {
    "banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
fruit=["banana",
"apple","orange",
"pear"]
print(stock,price)
for i in fruit:
    print(i,':')
    print('stock: ',stock[i])
    print('price: ' ,price[i])

total=0
for j in fruit:
    total+= price[j]*stock[j]
print('tổng: ',total)


        