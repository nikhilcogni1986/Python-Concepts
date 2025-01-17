fruits = ["Apples", "Bananas", "Oranges", "Pineapples"]
print(fruits)
print("Value at index 2 is: "+fruits[2])

# changing the value at particular index
fruits[2] = "Orange"
print("Modified list of fruits")
print(fruits)

# Appending a fruit to the list
fruits.append("Cherries")
print("After appending a value to a list")
print(fruits)

# removing element using pop()
fruits.pop()
print("Popping an element from the list")
print(fruits)

# Removing an element with index specified
fruits.pop(2)
print("Popping an element with specified index")
print(fruits)