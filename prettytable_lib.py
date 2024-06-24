from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Abra", "Appletun", "Arceus"])
table.add_column("Type", ["Psychic", ["Grass", "Dragon"], "Normal"])

table.align = "l"

print(table)
