from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

espresso = menu.find_drink('espresso')
latte = menu.find_drink('latte')
cappuccino = menu.find_drink('cappuccino')

is_on = True

while is_on:
    user_response = input(f"What would you like {menu.get_items()}? ").lower()
    if user_response == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_response == 'off':
        is_on = False
    else:
        drink = menu.find_drink(user_response)
        is_sufficient = coffee_maker.is_resource_sufficient(drink)
        if is_sufficient:
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)

