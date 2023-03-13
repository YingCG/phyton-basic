my_stuff = {"key1" : "value", "key2" : "value2","key3":{"123":[1,2,3,"grabMe"]}}
print(my_stuff["key2"])
print(my_stuff)
print(my_stuff['key3']['123'][3].upper())

menu ={'lunch':'sandwich', 'bfast':'egg on toast' }
menu['dinner'] = 'ramen'
menu['bfast'] ='peanut butter with sourdough'
print(menu['dinner'].upper())
print(menu['bfast'].upper())
print(menu)
