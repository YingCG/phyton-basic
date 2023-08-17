from coffee_menuitem import MenuItem

class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "chocolate" : 300
        }

    def resourcesIsSufficient(self, menuItem: MenuItem):
        return self.resources["water"] > menuItem.get_ingredient("water") \
            and self.resources["milk"] > menuItem.get_ingredient("milk") \
            and self.resources["coffee"] > menuItem.get_ingredient("coffee") \
            and self.resources["chocolate"] > menuItem.get_ingredient("chocolate")
    
    def make_coffee(self, menuItem: MenuItem):
        print(f"{menuItem.get_name()} is ready in 3 mins")
        self.resources["water"] -= menuItem.get_ingredient("water") 
        self.resources["milk"] = self.resources["milk"] - menuItem.get_ingredient("milk") 
        self.resources["coffee"] = self.resources["coffee"] - menuItem.get_ingredient("coffee") 
        self.resources["chocolate"] = self.resources["chocolate"] - menuItem.get_ingredient("chocolate") 
        print("Done!")