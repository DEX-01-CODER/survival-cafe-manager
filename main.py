"""
Survival Café Manager — Phase 1a (Procedural Coffee Machine)

Build this yourself by filling each TODO.
Keep prints inside the main loop; keep helpers returning data.
"""

# ---------- 1) DATA SETUP ----------
# Define the menu with available drinks, their ingredient requirements, and cost.
# This structure allows easy access to drink details and facilitates resource checks and transactions.
MENU = {
    # EXAMPLE structure; set your own numbers:
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

# Initialize the resources available in the machine.
# This keeps track of ingredient quantities and total money earned.
resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 300,
    "coins": 0.0,  # total money earned
}

# ---------- 2) HELPERS ----------
# These functions encapsulate key operations for managing the coffee machine,
# keeping the main loop clean and focused on user interaction.

def is_resource_sufficient(order_ingredients: dict) -> tuple[bool, str | None]:
    """
    Verify that the machine has enough ingredients for the requested drink.
    This prevents starting a transaction that cannot be fulfilled.
    Returns a tuple indicating sufficiency and the name of any missing ingredient.
    """
    for name, needed in order_ingredients.items():
        have = resources[name]
        if have < needed:
            return False, name
    return True, None


def process_coins() -> float:
    """
    Collect coin input from the user and calculate the total amount inserted.
    This simulates the payment process and returns the total money provided.
    """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)


def is_transaction_successful(payment: float, drink_cost: float) -> tuple[bool, float]:
    """
    Determine if the payment covers the drink cost.
    If payment is sufficient, update the machine's earnings and calculate change.
    Otherwise, indicate failure so the transaction can be canceled.
    """
    if payment < drink_cost:
        return False, 0.0
    change = round(payment - drink_cost, 2)
    resources["coins"] += drink_cost
    return True, change


def make_coffee(drink_name: str, order_ingredients: dict) -> None:
    """
    Deduct the ingredients used to make the drink from the machine's resources.
    This updates the inventory to reflect the consumed materials.
    """
    for name, quantity in order_ingredients.items():
        resources[name] -= quantity


# ---------- 3) MAIN LOOP ----------
# This loop drives the user interaction, handling commands and coordinating helper functions.
# It ensures the machine responds appropriately to user input and manages the coffee-making process.

def main():
    """
    Continuously prompt the user for input until the machine is turned off.
    Supports making drinks, reporting resources, and shutting down.
    Each step validates inputs, handles payments, and updates resources accordingly.
    """
    running = True
    while running:
        choice = input("What would you like? (espresso/latte/cappuccino) or 'report'/'off': ").strip().lower()

        if choice == "off":
            # Gracefully exit the program when the user decides to turn off the machine.
            break
        if choice == "report":
            # Provide a snapshot of current resource levels and total money earned.
            # Useful for monitoring and restocking.
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Coins: ${resources['coins']:.2f}")
            continue

        if choice not in MENU:
            # Handle invalid drink requests by guiding the user to valid options.
            print("Please choose: espresso, latte, or cappuccino. (Or 'report'/'off')")
            continue

        # Check if there are enough ingredients to make the selected drink before proceeding.
        ingredients = MENU[choice]["ingredients"]
        ok, missing = is_resource_sufficient(ingredients)
        if not ok:
            print(f"Sorry, not enough {missing}.")
            continue

        # Process the payment by collecting coins and verifying the transaction.
        cost = MENU[choice]["cost"]
        payment = process_coins()
        ok, change = is_transaction_successful(payment, cost)
        if not ok:
            print("Sorry that's not enough money. Money refunded.")
            continue
        if change > 0:
            print(f"Here is ${change:.2f} in change.")

        # Deduct ingredients and confirm the drink is ready to the user.
        make_coffee(choice, ingredients)
        print(f"Here is your {choice} ☕. Enjoy!")

    # Notify user that the machine is shutting down.
    print("Café turning off. Goodbye!")


if __name__ == "__main__":
    main()
