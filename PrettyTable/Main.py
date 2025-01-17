from prettytable import PrettyTable
table = PrettyTable()

# Add row by row
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtel", "Water"])
table.add_row(["Charmander", "Fire"])
print(table)