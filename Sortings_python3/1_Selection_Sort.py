# We start with a list, we want it to be sorted in ascending order
# First, we need arguments: list, current minimum and current item
# we iterate thru the list using current item, and we're looking for the smallest item.
# After we find it and make it to current minimum, we then place it at the start of a list - it creates clear part of a list, we do not touch it later on
# During second iteration, we're looking for another smallest element, we iterate with current item and when it is smaller than current minimum we change it to current minimum (both pointers are on it)
# At the end of a iteration current minimum gets placed after the first element and it goes until array is sorted

# now do it in python xd

# I'd love to make another list but then it wont be sorting will it

listA = [3, 4, 1, 7, 9, 20, 4, 6, -12, 8, 3, 3, 1, 2, 6, 5, 0, -4]
def selectionAlgorithm(list):
    elementsSorted = 0
    for i in range(0, len(list)):
        currMin = list[i]
        for j in range(elementsSorted, len(list)):
            currEl = list[j]
            if currMin > currEl:
                currMin = currEl
            else:
                continue
            list.insert(elementsSorted, list.pop(j))         
        elementsSorted += 1 # little tab here got me thinking for 15 minutes
    return list

print(selectionAlgorithm(listA))