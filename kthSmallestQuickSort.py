"""
Given List of N integers
find kth smallest element
Quick sort then find kth smallest
O(nlogn)
Algorithm 2: find the kth smallest element in the list using partition procedure of Quicksort recursively
Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
"""
import random
import time

def quickSort(unsorted, left, right):
    end = time.time()
    t = end - start
    print(f"{t:.04f} secs.")
    if left < right:
        splitPoint = partitionList(unsorted, left, right)
        
        quickSort(unsorted, left, splitPoint-1)
        quickSort(unsorted, splitPoint+1, right)

def partitionList(listToPart, left, right):
    pivot = listToPart[left] # picking first element as pivot point (non median)

    index = left + 1

    for currI in range(left+1, right+1):
        if listToPart[currI] <= pivot:
            listToPart[index], listToPart[currI] = listToPart[currI], listToPart[index]
            index += 1 

    listToPart[left], listToPart[index-1] = listToPart[index-1], listToPart[left]
    return index-1

# create an N size list with random values
def randomList(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(i, i+20))

    return lst

def getElement(kth, arr):
    return arr[kth-1]


if __name__ == "__main__":
    start = time.time()
    print("Random List Generated")
    arrSize = 512

    arr = randomList(arrSize)
    
    arr =  [3, 5, 12, 17, 5]
    print(arr)
    quickSort(arr, 0, len(arr)-1)
    k = random.randint(0, len(arr))
    print("Sorted: ", arr)
    
    print("Searhing random valid value after quickSort")
    print("K value: ", k, " - Element at K: ", getElement(k, arr))







