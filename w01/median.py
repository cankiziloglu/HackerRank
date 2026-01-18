import math


def findMedian(arr):
    length = len(arr)
    index = math.floor(length / 2)
    arr.sort()
    return arr[index]


# arr = input("array")
print(findMedian([5, 3, 1, 2, 4]))
