class MenuItem:
    """Represents an item on the coffee menu."""
    def __init__(self, name, cost, water, coffee, milk):
        """Initializes a MenuItem."""
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    def get_details(self):
        """Returns details about the menu item."""
        return f"{self.name} — ${self.cost} (water: {self.ingredients['water']}, milk: {self.ingredients['milk']}, coffee: {self.ingredients['coffee']})"

class Menu:
    """Represents the coffee menu."""
    def __init__(self):
        """Initializes the Menu."""
        self.menu = [
            MenuItem(name= "latte", water=200, milk = 150, coffee = 24, cost= 1.5),
            MenuItem(name= "espresso", water=50, milk = 0, coffee = 18, cost= 1.5),
            MenuItem(name= "cappuccino", water=250, milk = 100, coffee = 24, cost= 3.0)]

    def get_items(self):
        """Returns a list of available menu items."""
        return "/".join(item.name for item in self.menu)

    def find_item(self, name):
        """Finds a menu item by name."""
        for item in self.menu:
            if item.name == name:
                return item
        print("Sorry that item is not available.")

class CoffeeMaker():
    """Manages the coffee making process and resources."""
    def __init__(self):
        """Initializes the CoffeeMaker."""
        self.resources = {
            "water": 1000,
            "milk": 800,
            "coffee": 300
        }


    def report(self):
        """Prints a report of resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, menu_item):
        """Checks if there are enough resources for the menu item."""
        for name, needed in menu_item.ingredients.items():
            if needed > self.resources.get(name, 0):
                print(f"Sorry there is not enough {name}.")
                return False
        return True

    def make_coffee(self, menu_item):
        """Makes the coffee for the given menu item."""
        for name, used in menu_item.ingredients.items():
            self.resources[name] -= used

        print(f"Here is your {menu_item.name} ☕️. Enjoy!")


class MoneyMachine:
    """Handles all money transactions."""
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }
    def __init__(self):
        """Initializes the MoneyMachine."""
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints a report of money."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        self.money_received = 0
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return round(self.money_received, 2)


    def make_payment(self, cost):
        """Processes the payment for a menu item."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change:.2f} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
