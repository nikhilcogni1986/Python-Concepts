# Swap function
def swapList(newList):
    size = len(newList)

    # swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList


vegetables = ["Tomato", "Cauliflower", "Carrot", "Beetroot"]
print(swapList(vegetables))
