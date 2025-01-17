fruits = {"Apples": "Red",
          "Oranges": "Orange",
          "Cherries": "Red"
          }
print(fruits["Apples"])
print(fruits["Oranges"])
print(fruits["Cherries"])

print(len(fruits))

# Data types in the dictionary
carDetails = {
    "ModelName": "Ford",
    "ModelID": "CX100",
    "electric": "False",
    "colors": ["Red", "Orange", "Blue"]
}
print(carDetails["ModelName"])
print(carDetails["colors"])
print(type(carDetails))

modelDetails = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = modelDetails["model"]
print(x)

# get(key) is used to fetch the value
print(modelDetails.get("brand"))
