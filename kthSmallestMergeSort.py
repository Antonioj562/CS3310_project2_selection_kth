"""
Algorithm 1: find the kth smallest element in the list using the O (n log n) Mergesort sorting method.
"""
import random
import time

def merge(leftSide, rightSide):
    resArr = []
    i = 0
    j = 0

    while (i<len(leftSide) and j<len(rightSide)):
        if (leftSide[i] < rightSide[j]):
            resArr.append(leftSide[i])
            i += 1
        else:
            resArr.append(rightSide[j])
            j += 1
    resArr.extend(leftSide[i:])
    resArr.extend(rightSide[j:])
    return resArr

# Sort using Merge Sort Algorithm
def mergeSort(unsortedList):
    end = time.time()
    t = end - start
    print(f"{t:.04f} secs.")
    if (len(unsortedList) <= 1):
        return unsortedList
    
    mid = len(unsortedList) // 2
    left = unsortedList[:mid]
    right = unsortedList[mid:]

    sortLeft = mergeSort(left)
    sortRight = mergeSort(right)
    return merge(sortLeft, sortRight)




# create an N size list with random values
def randomList(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(i, i+20))

    return lst

def getElement(kth, arr):
    return arr[kth-1]


if __name__ == "__main__":

    print("Random List Generated")

    start = time.time()
    arrSize = 8192
    rLst = randomList(arrSize)
    # Testing list vs random testing
    rLst = [10, 5, 3, 8, 20]
    print(rLst)
    
    sorted = mergeSort(rLst)
    k = random.randint(1, len(rLst))

    print("Sorted: ", sorted)

    print("Searching random valid value")
    print("K - Element at K: ", k, " - ", getElement(k, sorted))
    # Take user input here to test
    



