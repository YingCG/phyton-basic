from coffee_menuitem import MenuItem

class Menu:
    def __init__(self):
        self.items =[
            MenuItem(1, "black coffee", 4.50, 50, 10, 0, 40),
            MenuItem(2, "hot chocolate", 5.50, 10 , 0, 50, 40)
        ]

    def print_menu(self):
        for item in self.items:
            print(f"{item.get_id()} - {item.get_name()} : {item.get_price()}")

    def find_item(self, id):
        for item in self.items:
            if id == item.get_id():
                return item

        return None       