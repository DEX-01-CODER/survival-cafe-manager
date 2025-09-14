from coffee_machine import Menu, MenuItem, CoffeeMaker, MoneyMachine


menu = Menu()
maker = CoffeeMaker()
cashier = MoneyMachine()

def main():
    """
    Continuously prompt the user for input until the machine is turned off.
    Supports making drinks, reporting resources, and shutting down.
    Each step validates inputs, handles payments, and updates resources accordingly.
    """
    running = True
    while running:
        choice = input(f"What would you like? ({menu.get_items()}) or 'report'/'off': ").strip().lower()

        if choice == "off":
            print("Café turning off. Goodbye!")
            break
        if choice == "report":
            # Provide a snapshot of current resource levels and total money earned.
            # Useful for monitoring and restocking.
            maker.report()
            cashier.report()
            continue

        item = menu.find_item(choice)
        if not item:
            print("Please choose a valid drink.")
            continue
        if not maker.is_resource_sufficient(item):
            continue
        if not cashier.make_payment(item.cost):
            continue
        maker.make_coffee(item)

if __name__ == "__main__":
    main()
