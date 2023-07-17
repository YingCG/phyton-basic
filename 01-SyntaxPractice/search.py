price_list = {
  'fish' : 18.99,
  'egg' : 12.50,
  'broccoli' : 3.50
}
print("Hello")

def find_price(item):
  if item in price_list:
    print(price_list.get(item))
    #return item
  else:
    print('not such item') 

find_price('bread')
