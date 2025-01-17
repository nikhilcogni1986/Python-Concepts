car = {
    "Model": "FD100",
    "Color": "Red",
    "Year": "2020"
}
x = car.keys()
print(x)

# Add an item to car dictionary
car["Manufacturer"] = "TATA"

# print dictionary
print(car)

# get all values from the dictionary
print(car.values())

# Update the value to existing dictionary
car["Year"] = "2024"

# print the updated car dictionary
print(car)

# get the items from dictionary
car_items = car.items()
print(car)

# update the dictionary
car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car_dict.update({"manufacturer": 2020})
print(car_dict)
