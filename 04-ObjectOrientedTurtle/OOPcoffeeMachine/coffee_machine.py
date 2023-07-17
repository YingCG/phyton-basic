## Program Requirements

# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee

from coffee_maker import CoffeeMaker
from coffee_menu import Menu

coffee_Maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    menu.print_menu()
    choice = input("What number do you want?")
    order = menu.find_item(int(choice))
    if order is None:
        print("No such product")
        continue
    print(f"Preparing {order.get_name()}...")
    if not coffee_Maker.resourcesIsSufficient(order):
        print("Out of order")
        continue
    print(f"Total is : {order.get_price()}")
    coffee_Maker.make_coffee(order)
    is_on = input("Continue?") == "y"

