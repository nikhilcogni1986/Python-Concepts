# Loops in Dictionary
fruits = {
           "Apples": "Red",
           "Watermelon": "Green",
           "Grapes": "Purple"
}

# Print all keys of the dictionary
print("Print keys of fruit dictionary")
for fruit in fruits:
    print(fruit)

print("Print values of fruit dictionary")

# Print all values of the dictionary
for x in fruits:
    print(fruits[x])

print("Use values in loops to print items")
# use values in loops
for x in fruits.values():
    print(x)

print("Use keys in loops to print items")

# use keys in loops
for x in fruits.keys():
    print(x)