# each key can only have one value
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}


# to add more info, we nesting a List in a Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary
detail_travel_log = {
    "France" : {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 2},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5},
}

#Nesting Dictionary in a List
more_travel_log = [
    { 
         "country" : "France", 
         "cities_visited": ["Paris", "Lille", "Dijon"], 
         "total_visits" : 2
     },
    {
        "country" : "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits" : 5
    },    
]

def add_new_country(countryVisited, timesVisited, citiesVisited):
    new_country = {}
    new_country["country"] = countryVisited
    new_country["total_visits"] = timesVisited
    new_country["cities_visited"] = citiesVisited
    more_travel_log.append(new_country)

add_new_country("Malaysia", 14, ["Kuala Lumpur", "Ipoh", "Penang"])
# print(more_travel_log[country] )

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict["c"] = [1,2, 3]
print(dict)
#output --> {'a': 1, 'b': 2, 'c': [1, 2, 3]}

# for key in dict:
#     dict[key] +=1
# print(dict)

dict[1] = 4
print(dict)
#output --> {'a': 1, 'b': 2, 'c': [1, 2, 3], 1: 4}

print(dict[1])

# To print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2])
# output --> ['Steak']

print(order["main"][2][0])
