from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
is_sufficient = True
is_payment_successful = False

while is_on:
    # TODO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order_name = input(menu.get_items() + " ")

    # TODO 2 Turn off the Coffee Machine by entering “off” to the prompt
    if order_name == "off":
        is_on = False
        print("shutting down")

    # TODO 3 Print report.
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()

    # TODO 4 Check resources sufficient?
    else:
        drink = menu.find_drink(order_name)
        if not drink is None:
            is_sufficient = coffee_maker.is_resource_sufficient(drink)
        else:
            continue

        if is_sufficient:
            # TODO 5 Process coins
            is_payment_successful = money_machine.make_payment(drink.cost)

            # TODO 6 Check transaction successful?
            if is_payment_successful:
                # TODO 7 Make Coffee.
                coffee_maker.make_coffee(drink)
        else:
            continue

