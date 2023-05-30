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
another_travel_log = [
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

