# suppliers = ["Staplers", "Pencils", "Drawing sheets"]
# print(suppliers)
# print("------------------------------------")
#
# print(suppliers[0])
# print(suppliers[2])
#
# print("------------------------------------")
#
# for i in range(len(suppliers)):
#     print("Index " + str(i) + " in supplies is " + suppliers[i])
# print("------------------------------------")
#
# print("List concatenation using for loop")
# catnames = []
# while True:
#     print("Enter the name of cat " + str(len(catnames) + 1) + "( or enter nothing to stop)")
#     name = input()
#     if name == '':
#         break
#     catnames = catnames + [name]
# print("Cat Names are: ")
# for name in catnames:
#     print(name)
# print("------------------------------------")
# print("In and Not operators")
#
# pets = ['howdy', 'Loki', 'Bella']
# print("Enter a pet name: ")
# name = input()
# if name not in pets:
#     print("I don't have a pet with name " + name)
# else:
#     print("I have a pet with name " + name)

print("------------------------------------")
print("Multiple Assignment to variables")
cat = ['fat', 'black', 'cloud']
size, colour, disposition = cat

print("------------------------------------")
print("Index method of List")
sports = ['Cricket', 'Football', 'Tennis']
print(sports.index("Tennis"))

print("Checking if Tennis is in Sports List")
print(sports.__contains__('Tennis'))

print("Appending Rugby to sports List")
print(sports.append('Rugby'))
print(sports)

print("Remove last element from Sports List")
print(sports.pop())
print(sports)

print("Reverse and Print the sports List")
print(sports.reverse())
print(sports)

print("Sorting the sports list")
print(sports.sort())
print(sports)

print("Sorting the sports list in reverse")
print(sports.sort(reverse=True))
print(sports)

print("Sorting strings takes place in ASCII phatical order")
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
print(spam.sort())
print(spam)

print("Sorting the list with lower case first and then followed by Upper case")
print(spam.sort(key=str.lower))
print(spam)
