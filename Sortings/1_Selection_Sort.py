# We start with a list, we want it to be sorted in ascending order
# First, we need arguments: list, current minimum and current item
# we iterate thru the list using current item, and we're looking for the smallest item.
# After we find it and make it to current minimum, we then place it at the start of a list - it creates clear part of a list, we do not touch it later on
# During second iteration, we're looking for another smallest element, we iterate with current item and when it is smaller than current minimum we change it to current minimum (both pointers are on it)
# At the end of a iteration current minimum gets placed after the first element and it goes until array is sorted

# now do it in python xd