class CoffeeMachine:
    coffee_type = {
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

    def __init__(self, water_balance, milk_balance, coffee_balance, money):
        self.resources = {
            "water": water_balance,
            "milk": milk_balance,
            "coffee": coffee_balance,
            "money": money
        }

    def add_resources(self, water_balance, milk_balance, coffee_balance):
        self.resources["water"] += water_balance
        self.resources["milk"] += milk_balance
        self.resources["coffee"] += coffee_balance

    def get_money(self):
        money = self.resources["coffee"]
        self.resources["coffee"] = 0
        return money

    def get_report(self):
        return (f"Water: {self.resources["water"]} ml,\n"
                f"Milk: {self.resources["milk"]} ml,\n"
                f"Coffee: {self.resources["coffee"]} g,\n"
                f"Money: ${self.resources["money"]}\n")

    def buy_coffee(self, coffee_type):
        if coffee_type not in self.coffee_type:
            print("We dont have that one")
            return 0

        if not self.enough_resources(coffee_type):
            return 0

        money = self.insert_coin()

        success, change = self.change_count(coffee_type, money)
        if success:
            self.make_coffee(coffee_type)

        return change

    def enough_resources(self, coffee_type):
        coffee_resources = self.coffee_type[coffee_type]["ingredients"]

        for item in coffee_resources:
            if coffee_resources[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False

        return True

    def change_count(self, coffee_type, money):
        if self.coffee_type[coffee_type]["cost"] > money:
            print(f"Sorry, that`s not enough money. Money refunded: ${money}")
            return False, money

        self.resources["money"] += self.coffee_type[coffee_type]["cost"]
        money -= self.coffee_type[coffee_type]["cost"]
        print(f"Here is ${money} in change")

        return True, money

    def make_coffee(self, coffee_type):
        coffee_resources = self.coffee_type[coffee_type]["ingredients"]

        for item in coffee_resources:
            self.resources[item] -= coffee_resources[item]

        print(f"Here is your {coffee_type}. Enjoy!")

    def insert_coin(self):
        quoters = int(input("How many quoters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))

        return ((quoters*0.25)
                 + (dimes*0.10)
                 + (nickles*0.05)
                 + (pennies*0.01))


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(300, 200, 100, 10)
    while True:
        choice = input("What would you like? espresso|latte|cappuccino   ")

        if choice == "off":
            print("Goodbye!")
            break

        if choice == "report":
            print(coffee_machine.get_report())
        else:
            coffee_machine.buy_coffee(choice)

