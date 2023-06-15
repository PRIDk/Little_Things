# so basically bubble sort pushes biggest element of a list to the end of it
# O(n^2)
listA = [3, 4, 1, 7, 9, 20, 4, 6, -12, 5, 3, 3, 1, 2, 6, 5, 0, -4]

def bubbleSort(list):
    N = len(list)
    for i in range(1, N):
        for j in range(0, N-1):
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1] , list[j]       
            else:
                continue
    return list

print(bubbleSort(listA))