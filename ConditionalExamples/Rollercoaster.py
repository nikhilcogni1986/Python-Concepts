print("Welcome to the Rollercoaster!")
height = int(input("Enter the height in cms: "))
bill = 0
if height >= 120:
    print("You are allowed for the rollercoaster ride!")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
        print("Child tickets cost $5!")
    elif age <= 18:
        bill = 7
        print("Youth tickets cost $7")
    elif age >= 45 and age <=55:
        print("Everything will be ok you have free ticket")
    else:
        bill = 12
        print("Adult tickets cost $12")

    wants_photo = input("Do yu want the phot type Y for Yes and N for No")

    if wants_photo == "Y":
        bill = bill + 3
    print(f"Your final bill is ${bill}")

else:
    print("You are not allowed for the ride")
