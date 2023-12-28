from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffe_maker = CoffeeMaker()
payment = MoneyMachine()



machine_on = True
while machine_on:
    
    options = menu.get_items()
    choice = str(input(f'What would you like to order? {options}'))

    if choice == "off":
        print("Shutting down...")
        machine_on = False
    elif choice == "report":
        coffe_maker.report()
        payment.report()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        coffe_maker.is_resource_sufficient(drink) and payment.make_payment(drink.cost)
        coffe_maker.make_coffee(drink)
    else:
        print("Please choose a valid option.")