from day16_menu import Menu, MenuItem
from day16_coffee_maker import CoffeeMaker
from day16_money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


ion = True

while on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ")
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
