from replit import clear

print("Welcome to the secret auction program")
bids = {}
while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bids[name] = bid
    if input("Are there any other bidders? yes|no? ").lower() == "no":
        clear()
        break
    clear()

winner = ''
max = 0
for key, val in bids.items():
    if val >= max:
        winner = key
        max = val

print(f"The winner is {winner} with a bid of {max}")