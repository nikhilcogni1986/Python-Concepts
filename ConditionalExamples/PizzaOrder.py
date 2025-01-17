print("Welcome to Python pizza deliveries")

size = input("Enter the size of the pizza you want S, M, L ")
pepperoni = input("Do you want pepperoni on your pizza Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N ")
final_bill = 0
bill = 0
if size == "S":
    if pepperoni == "Y":
        bill = 17
    else:
        bill = 15

elif size == "M":
    if pepperoni == "Y":
        bill = 23
    else:
        bill = 20
else:
    if pepperoni == "Y":
        bill = 28
    else:
        bill = 25

if extra_cheese == "Y":
    final_bill = bill + 1
else:
    final_bill = bill

print(f"Final bill for the pizza order is: {final_bill}")
