from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True

while is_on:
    user_response = input(f"What would you like ({menu.get_items()})? ").lower()
    if user_response == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_response == 'off':
        is_on = False
    else:
        drink = menu.find_drink(user_response)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

