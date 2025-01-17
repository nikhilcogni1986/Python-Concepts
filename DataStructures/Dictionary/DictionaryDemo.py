spam = {"language": "Python", "Species": "Rat", "Sports": "Cricket"}
eggs = {"Species": "Rat", "Sports": "Cricket", "language": "Python"}
print(eggs == spam)
print(spam["language"])

# Print the dictionary using values and keys method
for value in spam.values():
    print(value)

print("--------------------------------------")
print("Printing the keys")
for key in spam.keys():
    print(key)

print("--------------------------------------")
print("Printing the values")
for i in spam.items():
    print(i)

print("--------------------------------------")
print("Printing the keys and values")
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + value)


print("--------------------------------------")
print("Check whether a key or value exists in Dictionary")
print("Species" in eggs.keys())
print("Cricket" in spam.values())

picnicItems = {"Fruits": "Apples", "Umbrellas": "2"}
print('I am bringing '+str(picnicItems.get('Fruits', "Bananas")))
print('I am bringing '+str(picnicItems.get('ExoticFruits', "Bananas")))

picnicItems.setdefault('snacks', 'Chips')
print(picnicItems)