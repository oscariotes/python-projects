from artwork import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

income = 0

def display_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${income}")

def is_resource_sufficient(order_ingredients):
    # Iterate over each item in the order ingredients dictionary
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:       
            print(f"Sorry there is not enough {item}.")     
            return False
    return True

def receive_coin_input():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def is_enough_money(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global income
        income += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def brew_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

coffee_machine_on = True

while coffee_machine_on:
    print(logo)
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_order == "off":
        print("Shutting down...")
        coffee_machine_on = False
    elif user_order == "report":
        display_report()
    else:
        if user_order in MENU:
            selected_drink = MENU[user_order]
            if is_resource_sufficient(selected_drink["ingredients"]):
                payment = receive_coin_input()
                if is_enough_money(payment, selected_drink["cost"]):
                    brew_coffee(user_order, selected_drink["ingredients"])
        else:
            print("Please choose a valid option.")
