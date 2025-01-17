# Prompt the user which flavour of coffee are they looking for
# expresso, latte, cappuccino
# Store the input and decide next
# When user prompts print report it should print resource values: Water: 100ml
# Milk: 50ml, Coffee: 76g, Money: $2.5
# Create a dictionary embedding coffee types, ingredients, and cost

MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

profit = 0
# Decide when to stop asking the user with a prompt
is_on = True


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def is_transaction_successful(money_received, cost_of_drink):
    """Returns True if money is sufficient else False"""
    if money_received >= cost_of_drink:
        global profit
        profit += cost_of_drink
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is your {change} change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coins():
    """This function calculates the total value of coins
    inserted and returns to calling function"""
    print("Please insert coins!")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def make_drink(drink_name, order_ingredients):
    """Reduce the ingredients based on the drink is prepared"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")


while is_on:
    choice = input("What would you like? (expresso/Latte/cappuccino)")
    if choice == "Off".lower():
        is_on = False
    elif choice == "Report".lower():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])

