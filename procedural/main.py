from art import logo
print(logo)

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
             'coffee': 18,
             'milk': 0,
        },
        'cost' : 1.50,
    },
    'latte': {
        'ingredients': {
            'water': 200,
             'coffee': 24,
             'milk': 150,
        },
        'cost' : 2.50,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
             'coffee': 24,
             'milk': 100,
        },
        'cost' : 3.00,
    }
}


resources = {
    'water' : 300,
    'coffee' : 100,
    'milk' : 200,
    'money_in_machine' : 0,
}

def calc_resources():
    resources['water'] -= MENU[user_choice]['ingredients']['water']
    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
    resources['milk'] -= MENU[user_choice]['ingredients']['milk']

while True:
    user_choice = input(f"\nWhat do you want? (espresso: ${MENU['espresso']['cost']} / latte: ${MENU['latte']['cost']} / cappuccino: ${MENU['cappuccino']['cost']})\nOr you can just check the resources: ").lower()

    if user_choice == "resources":
        print(f"Water: {resources['water']}\nCoffee: {resources['coffee']}\nMilk: {resources['milk']}\nMoney: ${resources['money_in_machine']}")
    elif user_choice not in MENU:
        print("Choose a valid option, please.")
    else:
        for item in MENU[user_choice]['ingredients']:
            if MENU[user_choice]['ingredients'][item] > resources[item]:
                print(f"Sorry, Not enough {item}, please come back later.")
                exit()

        else:
            user_choice_cost = MENU[user_choice]['cost']
            resources['money_in_machine'] += user_choice_cost

            print("Please enter the coins.")
            penny = int(input("How many Pennies? "))
            nickel = int(input("How many Nickels? "))
            dime = int(input("How many Dimes? "))
            quarter = int(input("How many Quarters? "))

            user_total = (penny * 0.01) + (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25)

            if user_total >= user_choice_cost:
                calc_resources()
                print(f"Here is your {user_choice} and your change: ${round(user_total - user_choice_cost,2)}. Enjoy!")
            else:
                print("Come back when you have money please.")
                break