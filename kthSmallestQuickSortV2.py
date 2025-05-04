"""
Algorithm 3: find the kth smallest element in the list using partition procedure of Quicksort recursively via Medians of Medians (mm).
Binary Search? for medians of medians>?????

"""
import random
import time

def quickSort(unsorted, left=0, right=None):
    end = time.time()
    t = end - start
    print(f"{t:.04f} secs.")
    if right is None:
        right = len(unsorted)-1

    if left < right:
        mediansPivot = medianOfMedians(unsorted[left:right+1])
        splitPoint = partitionList(unsorted, left, right, mediansPivot)

        quickSort(unsorted, left, splitPoint-1)
        quickSort(unsorted, splitPoint+1, right)

def insertionSort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = k
    return arr


def medianOfMedians(arr):
    if len(arr) <= 3:
        return insertionSort(arr)[len(arr)//2]
    
    sublists = []
    for i in range(0, len(arr), 5):
        chunk = arr[i:i + 5]
        sublists.append(chunk)  

    medians = []
    for sublist in sublists:
        inserted = insertionSort(sublist)[len(sublist)//2]
        medians.append(inserted)
    
    # Recursively calls the function to find the best median
    return medianOfMedians(medians)



def partitionList(listToPart, left, right, pivot):
    pivot =  listToPart[left]

    index = left + 1

    for currI in range(left+1, right+1):
        if listToPart[currI] <= pivot:
            listToPart[currI], listToPart[index] = listToPart[index], listToPart[currI]
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

    # print("Random List Generated")
    arrSize = 8192
    arr = randomList(arrSize)
    

    # arr = [20, 21, 2, 7, 21, 19]
    #print(arr)

    quickSort(arr, 0, len(arr)-1)
    k = random.randint(0, len(arr))
    #print("Sorted: ", arr)
    
    print("Searhing random valid value after quickSort")
    print("K value: ", k, " - Element at K: ", getElement(k, arr))



