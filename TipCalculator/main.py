print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))
total = (bill + (bill * tip_percent / 100)) /people_count
print(f"Each person should pay: ${total:.2f}")