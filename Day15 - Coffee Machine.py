run = True
cash = 0

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


def check_stock(drink):
    """
    Checks if there are enough ingredients in the resources to make the requested drink.
        
    Returns:
        bool: True if there are enough resources to make the drink, False otherwise.
    """
    ingredients = MENU[drink]["ingredients"]
    can_make = True
    for ingredient in ingredients:
        required_amount = ingredients[ingredient]
        available_amount = resources[ingredient]

        if required_amount > available_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            can_make = False
            break
    return can_make


def check_payment(drink, payment):
    """
    Checks the users payment vs the cost and will distribute change

    Returns:
        A print out of the change, or an appology in the case of insufficient funds
    """
    cost = MENU[drink]["cost"]
    if payment >= cost:
        global cash
        cash += cost
        change = payment - cost
        print(f"Here is your {drink} and ${change:.2f} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def take_payment():
    """
    Asks the user for the number of quarters, dimes, nickles, and pennies they have
    and calculates the total cash value.
    
    Returns:
        float: The total cash value based on the user's input.
    """
    quarter = int(input("how many Quarters do you have? "))
    dime = int(input("how many DIMES do you have? "))
    nickle = int(input("how many NICKLES do you have? "))
    penny = int(input("how many PENNIES do you have? "))
    cash = (quarter * .25) + (dime  * .10) + (nickle * .05)+(penny * .01)
    return cash



while run:
    customer_wants = input("What would you like? (espresso/latte/cappucino) ")
    if customer_wants.lower() == 'off':
        run = False
    elif customer_wants.lower() == 'report':
        for key, value in resources.items():
            print(key + ' = ' + str(value))
        print(f"cash = ${cash:.2f}")
    elif customer_wants.lower() in MENU.keys():
        drink = customer_wants.lower()
        if check_stock(drink):
            payment = take_payment()
            if check_payment(drink, payment):
                for ingredient, amount in MENU[drink]["ingredients"].items():
                    resources[ingredient] -= amount




# check transaction

# make cofee