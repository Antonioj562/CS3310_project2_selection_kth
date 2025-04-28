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
def quickSort(unsorted, left, right):
    if left < right:
        splitPoint = partitionList(unsorted, left, right)
        
        quickSort(unsorted, left, splitPoint-1)
        quickSort(unsorted, splitPoint+1, right)

def partitionList(listToPart, left, right):
    pivot = listToPart[0] # picking first element as pivot point (non median)

    index = left-1

    for currI in range(left, right):
        if listToPart[currI] <= pivot:
            index += 1 
            (listToPart[index], listToPart[currI]) = (listToPart[currI], listToPart[index])

    (listToPart[index+1], listToPart[right]) = (listToPart[right], listToPart[index+1])
    return index+1

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
    arrSize = 5
    rList = randomList(arrSize)
    print(rList)

    quickSort(rList, 0, len(rList)-1)
    sorted = rList
    k = random.randint(0, len(rList))
    print("Sorted: ", sorted)
    
    print("Searhing random valid value after quickSort")
    print("K value: ", k, " - Element at K: ", getElement(k, sorted))







