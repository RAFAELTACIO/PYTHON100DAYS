
menu = [
    ['espresso', 50, 18, 0, 150],
    ["latte", 200, 24, 150, 250],
    ['cappuccino', 250, 24, 100, 300]
]  # name, water, coffee, milk, price

resourcesmachine = [300, 100, 200]  # water, coffee, milk
moneymachine = 0

def sum_money(value):
    global moneymachine
    moneymachine += value

def payment(coffee):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennys = int(input("How many pennys?: "))

    total = (quarters * 25) + (dimes * 10) + (nickles * 5) + (pennys)

    for i in menu:
        if coffee == i[0]:
            price = i[4]

    if total >= price:
        if total == price:
            print("It is the exact value. No Change.")
            sum_money(price)
            return True
        if total > price:
            exchange = total - price
            sum_money(price)
            print(f'The exchange is {"%.2f" % (total - price)}.')
            return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def makecoffee(coffee):
    for i in menu:
        if coffee == i[0]:
            if resourcesmachine[0] >= i[1]:  # water
                if resourcesmachine[1] >= i[2]:  # coffee
                    if resourcesmachine[2] >= i[3]:  # milk
                        return True
                    else:
                        print("Milk not enough")
                        return False
                else:
                    print("Coffee not enough")
                    return False
            else:
                print("Water not enough")
                return False

def coffeemachine():
    while True:
        choosecoffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choosecoffee in ["espresso", "latte", "cappuccino"]:
            paid = payment(choosecoffee)
            if paid:
                resourceenough = makecoffee(choosecoffee)
                for i in menu:
                    if choosecoffee == i[0]:
                        resourcesmachine[0] -= i[1]  # water
                        resourcesmachine[1] -= i[2]  # coffee
                        resourcesmachine[2] -= i[3]  # milk
                if paid and resourceenough:
                    print(f"Here is your {choosecoffee} ☕. Enjoy!")
                elif paid and not resourceenough:
                    print("Sorry, that's not enough resources in the machine. Money refunded")
                    for i in menu:
                        if choosecoffee == i[0]:
                            resourcesmachine[0] += i[1]
                            resourcesmachine[1] += i[2]
                            resourcesmachine[2] += i[3]

        elif choosecoffee == "report":
            print(f'Water: {resourcesmachine[0]} ml.')
            print(f'Coffee: {resourcesmachine[1]} g.')
            print(f'Milk: {resourcesmachine[2]} ml.')
            print(f'Money: ${"%.2f" % (moneymachine / 100)}')

        elif choosecoffee == "off":
            print("Turning Off...")
            break
        else:
            print("Please select a valid option.")

coffeemachine()
