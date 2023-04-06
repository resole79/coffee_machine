from data import *


# Function to print the machine report
def str_report(resources_to_print, money=""):
    """Function to print the machine report
    accept:
    resources_to_print -> dict
    money -> float
    return:
    report_str -> str
    """
    water = resources_to_print["water"]
    milk = resources_to_print["milk"]
    coffee = resources_to_print["coffee"]

    report_str = f" - {water} ml - Water\n"
    report_str += f" - {milk} ml - Milk\n"
    report_str += f" - {coffee} gr - Coffee\n"
    if money:
        report_str += f" - {money} £ - Money\n"

    return report_str


# Function to simulate insert coin
def insert_coin():
    """ Function to simulate insert coin
    return:
    coin_insert -> float
    """
    quarters = ""
    dimes = ""
    nickles = ""
    pennies = ""

    while not quarters.isnumeric():
        quarters = input("How many quarters?: ")
    while not dimes.isnumeric():
        dimes = input("How many dimes?: ")
    while not nickles.isnumeric():
        nickles = input("How many nickles?: ")
    while not pennies.isnumeric():
        pennies = input("How many pennies?: ")

    quarters = int(quarters)
    dimes = int(dimes)
    nickles = int(nickles)
    pennies = int(pennies)

    coin_insert = (0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*pennies)

    return coin_insert


# Function to update resource
def update_resources(resource_user_ask):
    """
    Function to check resource machine
    accept:
    resource_user_ask -> dict
    """
    recipes = menu[resource_user_ask]["ingredients"]
    for ingredient in recipes:
        resources[ingredient] -= recipes[ingredient]


# Function to check resource machine
def check_resources_machine(resource_user_ask):
    """
    Function to check resource machine
    accept:
    resource_user_ask -> dict
    return:
    is_doable -> bool
    """
    is_doable = True
    recipes = menu[resource_user_ask]["ingredients"]
    for ingredient in recipes:
        if recipes[ingredient] > resources[ingredient]:
            print(f"\nSorry there is not enough {ingredient}")
            is_doable = False

    return is_doable


# Function to check if user put enough money
def check_enough_money(resource_user_ask, money):
    """
    Function to check if user put enough money
    accept:
    resource_user_ask -> dict
    money -> float
    return:
    is_doable -> bool
    """
    is_doable = True
    price = float(menu[resource_user_ask]["cost"])
    if price > money:
        print(f"\nSorry you insert £{money:.2f} that's not enough money. Money refunded.\n")
        is_doable = False
    elif price < money:
        change = money - price
        print(f"\nHere is £{change:.2f} in change.")

    return is_doable


off = False
print(logo)
print(str_report(resources))

while not off:
    display = f'- £{menu["espresso"]["cost"]} - Espresso\n'
    display += f'- £{menu["latte"]["cost"]} - Latte\n'
    display += f'- £{menu["cappuccino"]["cost"]} - Cappuccino\n'
    display += "What would you like? (espresso/latte/cappuccino): "

    user_ask = input(display).lower()

    if user_ask == "espresso" or user_ask == "latte" or user_ask == "cappuccino":
        if check_resources_machine(user_ask):
            coin_inserted = insert_coin()
            if check_enough_money(user_ask, coin_inserted):
                update_resources(user_ask)
                print(immagine_menu[user_ask])
                print(f"\nHere is your {user_ask}. Enjoy!")
                print("\nResources disponible")
                print(str_report(resources, menu[user_ask]["cost"]))
    elif user_ask == "report":
        print(str_report(resources))
    elif user_ask == "off":
        print("\nThe coffee machine is 'OFF' for maintainers.")
        print("Please try again later.")
        off = True
    else:
        print("\nSorry your choice are uncorrected!\n")
