from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu  = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()

while True:
    options = menu.get_items()
    user_choice = input(f"\nWhat do you want? ({options} priced at: $1.50/ $2.50/ $3.00):\n").lower()

    if user_choice == "off":
        break
    elif user_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee = coffe_maker.make_coffee(drink)









