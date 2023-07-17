class MenuItem:
    def __init__(self,id, name, price, water, coffee, chocolate, milk):
        self._id = id
        self._name = name
        self._price = price
        self._ingredients ={
            "water" : water,
            "coffee" : coffee,
            "chocolate" : chocolate,
            "milk" : milk
            }
    
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def get_ingredient(self, ingredientName):
        return self._ingredients[ingredientName]
    