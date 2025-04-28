"""
Algorithm 3: find the kth smallest element in the list using partition procedure of Quicksort recursively via Medians of Medians (mm).
Binary Search? for medians of medians>?????

"""
import random
def quickSort(unsorted, left, right):
    if left < right:
        splitPoint = partitionList(unsorted, left, right)
        
        quickSort(unsorted, left, splitPoint-1)
        quickSort(unsorted, splitPoint+1, right)

def partitionList(listToPart, left, right):
    pivot = len(listToPart)-1 // 2

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



